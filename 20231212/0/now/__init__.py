from time import time
from pathlib import Path
import atexit


path = Path("date")
if PATH.exists():
    DATE = float(PATH.read_text())
else:
    DATE = time()


@atexit.register
def writer():
    PATH.write_text(str(DATE))
