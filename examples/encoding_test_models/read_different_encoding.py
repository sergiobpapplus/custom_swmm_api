from pathlib import Path

from swmm_api import SwmmInput


def main():
    pth = Path(__file__).parent
    for fn in pth.iterdir():
        if fn.suffix == '.inp':
            inp = SwmmInput(fn)
            # print(inp._default_encoding)
            print(fn, inp.TITLE, '\n'*2)


if __name__ == '__main__':
    main()
