import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file, strip

def place_val(arr, val):
    arr.pop(0)
    index, done = 0, False
    while not done and index < len(arr):
        if val < arr[index]:
            arr.insert(index, val)
            done = True
        index += 1
    if not done:
        arr.append(val)

def find_max_cal(lines, top_n = 1):
    """
    Args:
        lines (list): all the food of the elves seperated by an empty string between each elves
        top_n (int, optional): Top n max calories carried by the elfs. Defaults to 1.

    Returns:
        _type_: Array of the n max calories carreid by elfs
    """
    top_n_values = [0 for _ in range(top_n)]
    lines.append("")
    current_val = 0
    for val in lines:
        if val == "":
            if current_val > top_n_values[0]:
                place_val(top_n_values, current_val)
            current_val = 0
        else:
            current_val += int(val)
    return top_n_values

if __name__ == "__main__":
    lines = read_txt_file("input")
    lines = list(map(strip, lines))
    print(f"Sum of 3 max amount of calories : {sum(find_max_cal(lines, top_n = 3))} calories")
    