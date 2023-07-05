import os
from glob import glob
from pathlib import Path
from typing import Generator


def get_app_names(dir_path: str | Path) -> Generator[str, None, None]:
    for _p in glob(os.path.join(dir_path, "*", "apps.py")):
        yield _p.split("/")[-2]
