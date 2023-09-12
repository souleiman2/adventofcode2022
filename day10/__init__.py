import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file, strip


def exec(lines):
    answer = 0
    x = 1
    cycle_nb = 0
    next_milestone = 20
    
    for line in lines:
        temp = line.split(" ")
        command, val = temp[0], None
        
        if len(temp) == 2:
            val = int(temp[1])
        
        if command == "noop":
            cycle_nb += 1
        else:
            cycle_nb += 2
            
            if cycle_nb >= next_milestone:
                answer += x*next_milestone
                next_milestone += 40
            
            x += val
            
    return answer


if __name__ == "__main__":
    lines = read_txt_file("input")
    lines = list(map(strip, lines))
    answer = exec(lines)
    print("Answer : ", answer)
    