import os.path
import sys

if sys.platform == 'linux':
    swmm_path_linux = os.path.join(os.path.dirname(__file__), 'swmm51015')
elif sys.platform.startswith('win'):
    pass
else:
    pass
