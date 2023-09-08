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


def score_path(matrix, pos, speed, init_val):
    current = pos + speed
    score = 0
    while current.x >= 0 and current.x < len(matrix[0]) and current.y >= 0 and current.y < len(matrix):
        if matrix[current.y][current.x] >= init_val:
            return score + 1
        score += 1
        current += speed
    return score
    

def score_pos(matrix, pos):
    val = matrix[pos.y][pos.x]
    
    return score_path(matrix, pos, Vector(-1, 0), val) * \
        score_path(matrix, pos, Vector(1, 0), val) * \
        score_path(matrix, pos, Vector(0, -1), val) * \
        score_path(matrix, pos, Vector(0, 1), val)

def max_score(matrix):
    score = -float('inf')
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            temp = score_pos(matrix, Vector(x,y))
            if temp > score:
                score = temp
    return score

if __name__ == "__main__":
    lines = read_txt_file("input")
    lines = list(map(strip, lines))
    matrix = [list(map(int, list(elem))) for elem in lines]
    print("Max Score : ", max_score(matrix))
    
    
    