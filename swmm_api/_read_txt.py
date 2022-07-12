import sys
import subprocess
import os
import warnings


def detect_encoding(filename):
    if "linux" in sys.platform:
        shell_output = subprocess.check_output(['file', '-i', filename]).decode().strip()
    else:
        try:
            cwd = os.path.dirname(filename)
            if not cwd:
                cwd = None
            shell_output = subprocess.check_output(f'bash -ic "file -i {os.path.basename(filename)}"',
                                                   cwd=cwd
                                                   ).decode().strip()
        except:
            try:
                import cchardet as chardet
                with open(filename, "rb") as f:
                    binary_txt = f.read()
                    detection = chardet.detect(binary_txt)
                    return detection["encoding"]
                    # confidence = detection["confidence"]
                    # txt1 = binary_txt.decode(encoding1)
            except:
                return 'utf-8'

    return shell_output.split('charset=')[-1]


def read_txt_file(filename, encoding=None):

    # import cchardet as chardet
    # with open(filename, "rb") as f:
    #     binary_txt = f.read()
    #     detection = chardet.detect(binary_txt)
    #     encoding1 = detection["encoding"]
    #     confidence1 = detection["confidence"]
    #     txt1 = binary_txt.decode(encoding1)

    if encoding is None:
        encoding = detect_encoding(filename)

    try:
        with open(filename, 'r', encoding=encoding) as file:
            txt = file.read()
    except UnicodeDecodeError:
        warnings.warn(f'Could not find correct encoding (found "{encoding}", but is wrong) for inp-file ("{filename}"). Please set encoding manually.')
        with open(filename, 'r') as file:
            txt = file.read()

    return txt
