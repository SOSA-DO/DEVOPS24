import shutil
from pathlib import Path

def copy_file(src, dest):
    srcfile = Path(srcfile)
    destfile = Path(destfile)

    shutil.move(srcfile, destfile)
    print(f'moved {srcfile} to {destfile}.  ')