
def read_txt_file(filename):
    f = open(filename + ".txt", "r")
    return f.readlines()

def strip(line):
    return line.strip()

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
    lines = read_txt_file("input")
    lines = list(map(strip, lines))
    print(f"Max amount of calories : {find_max_cal(lines)} calories")
    