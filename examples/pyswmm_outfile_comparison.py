import pandas as pd
from pathlib import Path
import time

from numpy import NaN

from swmm_api.output_file.extract import SwmmExtractValueError


def timeit(method):
    def timed(*args, **kwargs):
        # out_frames = getouterframes(currentframe())
        # frame_no = 1
        # frameinfo = out_frames[frame_no]
        #
        # s = signature(method)
        # arg_labels = list(s.parameters.keys())
        # for arg_used in kwargs.keys():
        #     arg_labels.remove(arg_used)

        # print(f'{frameinfo.filename}:{frameinfo.lineno}' + ': ' + container2tree(
        #     {method.__name__: ([str(i) + ' = ' + print_func(a) for i, a in zip(arg_labels, args)]
        #                        + [str(i) + ' = ' + print_func(p) for i, p in kwargs.items()]
        #                        # + ['==> {:0.4f}s'.format(te - ts)]
        #                        )
        #      }), end="\n")
        ts = time.perf_counter()
        result = method(*args, **kwargs)
        te = time.perf_counter()
        # print(f'   ==> {te - ts:0.4f}s\n')
        return te-ts

    return timed


@timeit
def read_pyswmm(fn):
    from pyswmm import Output
    from swmm.toolkit.shared_enum import SystemAttribute

    with Output(str(fn)) as out:
        ts = out.system_series(attribute=SystemAttribute.RUNOFF_FLOW)
    ts = pd.Series(ts)
    # return ts


@timeit
def read_swmm_api(fn):
    from swmm_api import SwmmOutput
    from swmm_api.output_file import OBJECTS, VARIABLES

    with SwmmOutput(fn) as out:
        ts = out.get_part(OBJECTS.SYSTEM, variable=VARIABLES.SYSTEM.RUNOFF)
    # return ts


@timeit
def read_swmm_api_slim(fn):
    from swmm_api import SwmmOutput
    from swmm_api.output_file import OBJECTS, VARIABLES

    with SwmmOutput(fn) as out:
        ts = out.get_part(OBJECTS.SYSTEM, variable=VARIABLES.SYSTEM.RUNOFF, slim=True, show_progress=False)
    # return ts


def get_all_out_files():
    import os

    li = []

    working_dir = Path(__file__).parent
    for root, dirs, files in os.walk(working_dir):
        root = Path(root)
        for file in files:
            if file.endswith('.out'):
                li.append(root / file)
    return li


suffixes = {
    "decimal": (" kB", " MB", " GB", " TB", " PB", " EB", " ZB", " YB"),
    "binary" : (" KiB", " MiB", " GiB", " TiB", " PiB", " EiB", " ZiB", " YiB"),
    "gnu"    : "KMGTPEZY",
}

# https://github.com/python-humanize/humanize/blob/main/src/humanize/filesize.py
def naturalsize(value: float | str, binary: bool = False, gnu: bool = False, format: str = "%.2f") -> str:
    """Format a number of bytes like a human readable filesize (e.g. 10 kB).
    By default, decimal suffixes (kB, MB) are used.
    Non-GNU modes are compatible with jinja2's `filesizeformat` filter.
    Examples:
        ```pycon
        >>> naturalsize(3000000)
        '3.0 MB'
        >>> naturalsize(300, False, True)
        '300B'
        >>> naturalsize(3000, False, True)
        '2.9K'
        >>> naturalsize(3000, False, True, "%.3f")
        '2.930K'
        >>> naturalsize(3000, True)
        '2.9 KiB'
        >>> naturalsize(10**28)
        '10000.0 YB'
        >>> naturalsize(-4096, True)
        '-4.0 KiB'
        ```
    Args:
        value (int, float, str): Integer to convert.
        binary (bool): If `True`, uses binary suffixes (KiB, MiB) with base
            2<sup>10</sup> instead of 10<sup>3</sup>.
        gnu (bool): If `True`, the binary argument is ignored and GNU-style
            (`ls -sh` style) prefixes are used (K, M) with the 2**10 definition.
        format (str): Custom formatter.
    Returns:
        str: Human readable representation of a filesize.
    """
    if gnu:
        suffix = suffixes["gnu"]
    elif binary:
        suffix = suffixes["binary"]
    else:
        suffix = suffixes["decimal"]

    base = 1024 if (gnu or binary) else 1000
    bytes_ = float(value)
    abs_bytes = abs(bytes_)

    if abs_bytes == 1 and not gnu:
        return "%d Byte" % bytes_

    if abs_bytes < base and not gnu:
        return "%d Bytes" % bytes_

    if abs_bytes < base and gnu:
        return "%dB" % bytes_

    for i, s in enumerate(suffix):
        unit = base ** (i + 2)

        if abs_bytes < unit:
            break

    ret: str = format % (base * bytes_ / unit) + s
    return ret


def main():
    res = {}
    for fn_out in get_all_out_files():
        print('_' * 10)
        print(f'{fn_out} | size={naturalsize(fn_out.stat().st_size)}')
        try:
            t1 = read_pyswmm(fn_out)
        except:
            t1 = NaN
        print(f'pyswmm       : {t1:0.4f}s')
        try:
            t2 = read_swmm_api(fn_out)
        except SwmmExtractValueError:
            t2 = NaN
        print(f'swmm_api     : {t2:0.4f}s')
        try:
            t3 = read_swmm_api_slim(fn_out)
        except SwmmExtractValueError:
            t3 = NaN
        print(f'swmm_api_slim: {t3:0.4f}s')

        res[naturalsize(fn_out.stat().st_size)] = {
            'pyswmm': t1,
            'swmm_api': t2,
            'swmm_api_slim': t2,
            'filename': str(fn_out)
        }
    print(pd.DataFrame(res).T.to_string())
    r"""
                 pyswmm  swmm_api swmm_api_slim                                                                                                                              filename
    6.25 kB    0.000961  0.001268      0.001268                                                             C:\Users\mp\PycharmProjects\swmm_api\examples\inp_test_encoding_utf-8.out
    341 Bytes       NaN  0.002007      0.002007                                                                                C:\Users\mp\PycharmProjects\swmm_api\examples\temp.out
    136.73 MB  0.954510  0.081560      0.081560                                                                               C:\Users\mp\PycharmProjects\swmm_api\examples\temp1.out
    5.75 MB    0.038542  0.005199      0.005199                                                                C:\Users\mp\PycharmProjects\swmm_api\examples\spn10\Example6-Final.out
    819.17 kB  0.010244  0.002282      0.002282                                                 C:\Users\mp\PycharmProjects\swmm_api\examples\epaswmm5_apps_manual\Example7-Final.out
    5.89 MB    0.038408  0.013278      0.013278  C:\Users\mp\PycharmProjects\swmm_api\examples\epaswmm5_apps_manual\Example6-Final_AllSections_GUI\Example6-Final_AllSections_GUI.out
    34.82 MB   2.287845  0.029642      0.029642                                                         C:\Users\mp\PycharmProjects\swmm_api\examples\surface_runoff_error\one_sc.out
    """


if __name__ == '__main__':
    main()
