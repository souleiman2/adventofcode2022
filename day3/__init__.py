import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file, strip

def find_priority(letter):
    if ord("a") <= ord(letter) <= ord("z"):
        return ord(letter) - ord("a") + 1
    return ord(letter) - ord("A") + 27

def find_similar(first_string, second_string):
    first_letters = sorted(first_string)
    second_letters = sorted(second_string)
    
    index_first, index_second = 0, 0
    while index_first < len(first_letters) and index_second < len(second_letters):
        if first_letters[index_first] == second_letters[index_second]:
            return first_letters[index_first]
        elif first_letters[index_first] < second_letters[index_second]:
            index_first += 1
        else:
            index_second += 1
    raise ValueError("There seems to be no similar value in both containers")

def calc_score_line(line):
    first_container, second_container = line[:len(line)//2], line[len(line)//2:]
    similar_letter = find_similar(first_container, second_container)
    return find_priority(similar_letter)

if __name__ == "__main__":
    lines = read_txt_file("input")
    lines = list(map(strip, lines))
    scores = list(map(calc_score_line, lines))
    print(f"Here is the sum of all the priorities : {sum(scores)}")
    
    