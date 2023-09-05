import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file

def is_all_diff(substr):
    return len(list(set(substr))) == len(substr)

def find_start_pos(line):
    index = 0
    size_substr = 14
    while index < len(line) - size_substr + 1:
        if is_all_diff(line[index:index+size_substr]):
            return index + size_substr
        index += 1


if __name__ == "__main__":
    line = read_txt_file("input")[0]
    line = line.strip()
    print("Answer : ", find_start_pos(line))
    
    
    