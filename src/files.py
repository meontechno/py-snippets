from pathlib import Path

from structlog import get_logger

logger = get_logger()


def list_all_files(directory: Path, patterns: list) -> list:
    if not isinstance(directory, Path):
        raise TypeError("Invalid path type")
    images_list = list()
    for pattern in patterns:
        images_list.extend([str(x) for x in directory.rglob(pattern)])
    return images_list
