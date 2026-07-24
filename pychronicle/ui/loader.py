from pathlib import Path


def load_source_code(file_path: Path) -> str:

    with open(file_path, "r", encoding="utf-8") as file:

        lines = file.readlines()

    numbered = []

    for number, line in enumerate(lines, start=1):

        numbered.append(
            f"{number:>3} │ {line.rstrip()}"
        )

    return "\n".join(numbered)