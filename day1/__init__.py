import sys
sys.path.append('..') # to be able to import files from parent directory
from .. import utils

def find_max_cal(lines):
    """
    Args:
        lines (list): all the food of the elves seperated by an empty string between each elves

    Returns:
        int: max amount of calories caried by a single Elf
    """
    lines.append("")
    max_val = 0
    current_val = 0
    for val in lines:
        if val == "":
            if current_val > max_val:
                max_val = current_val
            current_val = 0
        else:
            current_val += int(val)
    return max_val

if __name__ == "__main__":
    lines = utils.read_txt_file("input")
    lines = list(map(utils.strip, lines))
    print(f"Max amount of calories : {find_max_cal(lines)} calories")
    