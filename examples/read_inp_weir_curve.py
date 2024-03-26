from swmm_api import SwmmInput


def main():
    inp = SwmmInput('weir_test.inp')
    inp.force_convert_all()
    inp3a = inp.copy()
    inp3a.force_convert_all()

    inp.to_string()

    inp2a = SwmmInput.read_text(inp3a.to_string(fast=False))
    inp2a.force_convert_all()
    inp2b = SwmmInput.read_text(inp3a.to_string(fast=True))
    inp2b.force_convert_all()

    inp3b = inp.copy()
    inp3b.force_convert_all()
    print()


if __name__ == '__main__':
    main()
