import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file, strip

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return other.__add__(self)


def is_visible_path(matrix, pos, speed, init_val):
    current = pos + speed
    while current.x >= 0 and current.x < len(matrix[0]) and current.y >= 0 and current.y < len(matrix):
        if matrix[current.y][current.x] >= init_val:
            return False
        current += speed
    return True

def is_visible(matrix, pos):
    val = matrix[pos.y][pos.x]
    if pos.y == 0 or pos.y == len(matrix) -1 or pos.x == 0 or pos.x == len(matrix[0]) - 1:
        return True
    
    if is_visible_path(matrix, pos, Vector(-1, 0), val) or \
        is_visible_path(matrix, pos, Vector(1, 0), val) or \
        is_visible_path(matrix, pos, Vector(0, -1), val) or \
        is_visible_path(matrix, pos, Vector(0, 1), val):
        return True
    return False

def count_visible(matrix):
    count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if is_visible(matrix, Vector(x,y)):
                count += 1
    return count

if __name__ == "__main__":
    lines = read_txt_file("input")
    lines = list(map(strip, lines))
    matrix = [list(map(int, list(elem))) for elem in lines]
    print("Nb of visible : ", count_visible(matrix))
    
    
    