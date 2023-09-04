import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file

import re

def transfer(stacks, nb_from, nb_to, amount):
    stacks[nb_to] += stacks[nb_from][len(stacks[nb_from])-amount:][::-1]
    stacks[nb_from] = stacks[nb_from][:-amount]

def exec_all_transfer(stacks, lines):
    for line in lines:
        amount, nb_from, nb_to = list(map(int, re.findall(r'\d+', line)))
        
        transfer(stacks, nb_from - 1, nb_to -1, amount)
    
def extract_line_info(line, step = 4, offset = 1):
    return [line[offset+i*step] for i in range(len(line)//step + 1)]

def parse_stack(stack_lines):
    stack_lines = stack_lines[::-1]
    stack_lines = stack_lines[1:]
    data_matrix = [extract_line_info(line) for line in stack_lines]
    stacks = [[] for _ in range(len(data_matrix[0]))]
    for i in range(len(data_matrix[0])):
        j = 0
        while j < len(data_matrix) and data_matrix[j][i] != " ":
            stacks[i].append(data_matrix[j][i])
            j += 1
    return stacks

def split_stack_and_commands(lines):
    index_empty = lines.index("")
    return lines[:index_empty], lines[index_empty + 1:]

if __name__ == "__main__":
    lines = read_txt_file("input")
    lines = list(map(lambda x : x[:-1], lines))
    stack_lines, command_lines = split_stack_and_commands(lines)
    stacks = parse_stack(stack_lines)
    exec_all_transfer(stacks, command_lines)
    
    mess = ""
    for stack in stacks:
        mess += stack[-1]
    print(mess)
    
    
    