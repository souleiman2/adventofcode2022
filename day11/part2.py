import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file, strip
import math

def lcm(*integers):
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // math.gcd(a, b)
    return a

class Monkey:
    def __init__(self, items, worry_func, passing_func, ppcm = None):
        self.items = items
        self.worry_func = worry_func
        self.passing_func = passing_func
        self.ppcm = ppcm
    
    def add_item(self, item):
        self.items.append(item)
    
    def set_ppcm(self, ppcm):
        self.ppcm = ppcm
        
    def next_iter(self):
        passing_index = []
        for item in self.items:
            worry_level = self.worry_func(item)
            if self.ppcm is not None:
                worry_level %= self.ppcm
            passing_index.append((self.passing_func(worry_level), worry_level))
        self.items = []
        return passing_index

    def __str__(self):
        return str(self.items)

def parse_leaf(str_val):
    str_val = str_val.strip()
    if str_val == "old":
        return lambda x : x
    elif str_val.isdigit():
        return lambda x : int(str_val)

def parse_operation(str_func):
    str_func = str_func.strip()

    if "*" in str_func:
        first, second = str_func.split("*")
        return lambda x : parse_leaf(first)(x) * parse_leaf(second)(x)
    elif "+" in str_func:
        first, second = str_func.split("+")
        return lambda x : parse_leaf(first)(x) + parse_leaf(second)(x)

def parse_passing_rules(lines):
    divider = int(lines[0].split(" ")[-1])
    true_val = int(lines[1].split(" ")[-1])
    false_val = int(lines[2].split(" ")[-1])
    return lambda val : true_val if val % divider == 0 else false_val
    

def lines_to_monkey(lines):
    items = [int(elem) for elem in lines[0].split(":")[1].strip().split(", ")]
    worry_func = parse_operation(lines[1].split("=")[1].strip())
    passing_func = parse_passing_rules(lines[2:])
    return Monkey(items, worry_func, passing_func), int(lines[2].split(" ")[-1])
    
def sep_lines_in_group(lines):
    quant_monkey = 0
    groups_lines = []
    while quant_monkey < (len(lines) + 1) // 7:
        groups_lines.append(lines[quant_monkey*7+1:(quant_monkey+1)*7-1])
        quant_monkey += 1
    return groups_lines

def counting_items(monkeys):
    counts = [0 for _ in range(len(monkeys))]
    
    for _ in range(10000):
        for monkey_index, monkey in enumerate(monkeys):
            arr_passing_items = monkey.next_iter()
            counts[monkey_index] += len(arr_passing_items)

            for index, item in arr_passing_items:
                monkeys[index].add_item(item)
        
    return counts  

def final_answer(counts):
    max_val = max(counts)
    counts.pop(counts.index(max_val))
    return max_val*max(counts)


if __name__ == "__main__":
    lines = read_txt_file("input")
    lines = list(map(strip, lines))
    lines_group = sep_lines_in_group(lines)
    temp = list(map(lines_to_monkey, lines_group))
    monkeys, ppcm_vals = [], []
    for temp1, temp2 in temp:
        monkeys.append(temp1)
        ppcm_vals.append(temp2)
    
    ppcm = lcm(*ppcm_vals)
    
    for i in range(len(monkeys)):
        monkeys[i].set_ppcm(ppcm)
    
    counts = counting_items(monkeys)
    print("Counts : ", counts)
    print("Answer : ", final_answer(counts))
    