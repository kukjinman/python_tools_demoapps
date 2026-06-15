import sys
from pathlib import Path


def resource_path(*parts):
    base_dir = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base_dir.joinpath(*parts)


def output_path(*parts):
    if getattr(sys, "frozen", False):
        base_dir = Path(sys.executable).resolve().parent
    else:
        base_dir = Path(__file__).resolve().parent
    return base_dir.joinpath(*parts)
