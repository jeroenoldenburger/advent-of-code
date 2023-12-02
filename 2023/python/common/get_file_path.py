from pathlib import Path


def get_file_path(filename: str) -> Path:
    path_2023 = Path(__file__).parent.parent.parent
    return  path_2023 / filename