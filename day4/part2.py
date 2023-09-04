import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file, strip

def overlap(first_interval, second_interval):
    return first_interval[0] <= second_interval[1] and first_interval[1] >= second_interval[0]

def is_interval_included(line):
    first, second = line.split(",")
    first_interval, second_interval = list(map(int, first.split("-"))), list(map(int, second.split("-")))
    return overlap(first_interval, second_interval)

if __name__ == "__main__":
    lines = read_txt_file("input")
    lines = list(map(strip, lines))
    lines_fully_contained = list(map(is_interval_included, lines))
    print("Answer : ", sum(lines_fully_contained))