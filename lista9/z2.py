from pathlib import Path
import os
import re


def pdf(path):
    directory = Path(f"{path}\\")
    if directory.exists():
        files = []
        pattern = r"^(.*praca.*)\.(pdf)$"
        for dirpath, dirname, filenames in os.walk(directory):
            for file in filenames:
                if re.match(pattern, str(file)):
                    files.append(f"{dirpath}\\{file}")
        print('\n'.join(files))
    else:
        print('Podana ścieżka nie istnieje')
        exit(0)


if __name__ == "__main__":
    pdf('z2')
