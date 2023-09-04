import sys
sys.path.append('..') # to be able to import files from parent directory
from .. import utils

def find_priority(letter):
    if ord("a") <= ord(letter) <= ord("z"):
        return ord(letter) - ord("a") + 1
    return ord(letter) - ord("A") + 27

def find_similar(first_string, second_string):
    first_letters = sorted(first_string)
    second_letters = sorted(second_string)
    
    similar = set()
    index_first, index_second = 0, 0
    while index_first < len(first_letters) and index_second < len(second_letters):
        if first_letters[index_first] == second_letters[index_second]:
            similar.add(first_letters[index_first])
            index_first += 1
            index_second += 1
        elif first_letters[index_first] < second_letters[index_second]:
            index_first += 1
        else:
            index_second += 1
    return ''.join(similar)

def calc_group_lines(lines):
    current_line = lines[0]
    for i in range(1, len(lines)):
        current_line = find_similar(current_line, lines[i])
    return find_priority(current_line)

def group_lines(lines, group_size = 3):
    return [lines[i*group_size:(i+1)*group_size] for i in range(len(lines)//group_size)]

if __name__ == "__main__":
    lines = utils.read_txt_file("input")
    lines = list(map(utils.strip, lines))
    grouped_lines = group_lines(lines)
    scores = list(map(calc_group_lines, grouped_lines))
    print(f"Here is the sum of all the priorities : {sum(scores)}")