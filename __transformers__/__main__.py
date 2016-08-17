from runpy import run_module
from pathlib import Path
import sys

from . import setup

setup()

del sys.argv[0]

if sys.argv[0] == '-m':
    del sys.argv[0]
    run_module(sys.argv[0])
else:
    # rnupy.run_path ignores meta_path for first import
    path = Path(sys.argv[0]).parent.as_posix()
    module_name = Path(sys.argv[0]).name[:-3]
    sys.path.insert(0, path)
    run_module(module_name)
