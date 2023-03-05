import ast
from pathlib import Path

working_dir = Path(__file__).parent

import sys
sys.path.append(str(working_dir.parent.parent.parent))

from swmm_api.input_file import macros


def main():
    # module = dir(macros)
    # print(dir(macros))

    with open(working_dir / 'macros.rst', 'w') as f:

        _header = 'Input File Manipulation - Macros'
        f.write(_header + '\n')
        f.write('-'*len(_header) + '\n')

        for file in Path(macros.__file__).parent.iterdir():
            if file.stem.startswith('_'):
                continue
            print(file.stem)

            f.write('\n' + file.stem.replace('_', ' ').capitalize() + '\n')
            f.write('~'*len(file.stem) + '\n\n')

            f.write(f'.. currentmodule:: {macros.__package__}.{file.stem}\n')

            f.write('.. autosummary::\n')
            f.write('    :toctree: macros/\n\n')

            with open(file, encoding='utf-8') as _f:
                for part in ast.parse(_f.read()).body:
                    if isinstance(part, ast.FunctionDef):
                        if not part.name.startswith('_'):
                            f.write(f'    {part.name}\n')

if __name__ == '__main__':
    main()
