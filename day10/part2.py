import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file, strip


def exec(lines):
    x = 1
    cdr = ""
    position = 0
    
    for line in lines:
        temp = line.split(" ")
        command, val = temp[0], None
        
        if command == "noop":
            if x - 1 <= position <= x + 1:
                cdr += "#"
            else:
                cdr += "."
            
            position += 1
            
            if position == 40:
                cdr += "\n"
                position = 0
            
        else:
            val = int(temp[1])
            
            if x - 1 <= position <= x + 1:
                cdr += "#"
            else:
                cdr += "."
            position += 1
            
            if position == 40:
                cdr += "\n"
                position = 0
            
            if x - 1 <= position <= x + 1:
                cdr += "#"
            else:
                cdr += "."
            position += 1
            
            if position == 40:
                cdr += "\n"
                position = 0
            
            x += val
            
    print(cdr)


if __name__ == "__main__":
    lines = read_txt_file("input")
    lines = list(map(strip, lines))
    exec(lines)
    