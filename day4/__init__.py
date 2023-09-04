import sys
sys.path.append('..') # to be able to import files from parent directory
from .. import utils


if __name__ == "__main__":
    lines = utils.read_txt_file("input")
    lines = list(map(strip, lines))
    scores = list(map(calc_score_line, lines))
    print(f"Here is the sum of all the priorities : {sum(scores)}")
    