import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file, strip


if __name__ == "__main__":
    lines = read_txt_file("input")
    lines = list(map(strip, lines))
    