import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file, strip

from enum import Enum

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def opp(self):
        return Vector(-self.x, -self.y)
    
    def __rmul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return other.__add__(self)

    def clone(self):
        return Vector(self.x, self.y)
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

def move_vec_to_direction_scalar(move_vec):
    if move_vec.y > 0:
        return Direction.UP.value, abs(move_vec.y)
    elif move_vec.y < 0:
        return Direction.DOWN.value, abs(move_vec.y)
    elif move_vec.x > 0:
        return Direction.RIGHT.value, abs(move_vec.x)
    return Direction.LEFT.value , abs(move_vec.x)

class Direction(Enum):
    UP = Vector(0, 1)
    DOWN = Vector(0, -1)
    LEFT = Vector(-1, 0)
    RIGHT = Vector(1, 0)

class Knot:
    def __init__(self, pos : Vector):
        self.__pos = pos
    
    @property
    def x(self):
        return self.__pos.x

    @property
    def y(self):
        return self.__pos.y
    
    def is_next_to_knot(self, next_knot):
        return abs(self.x - next_knot.x) <= 1 and abs(self.y - next_knot.y) <= 1
    
    def move(self, next_knot):
        if not self.is_next_to_knot(next_knot):
            vec = Vector(0,0)
            
            if self.x > next_knot.x:
                vec.x = -1
            elif self.x < next_knot.x:
                vec.x = 1
                
            if self.y > next_knot.y:
                vec.y = -1
            elif self.y < next_knot.y:
                vec.y = 1
            
            self.__pos += vec

    def move_direction(self, direction):
        self.__pos += direction

class Rope:
    def __init__(self, starting_pos, number_knot):
        self.knots = [Knot(starting_pos) for _ in range(number_knot)]
        self.tail_pos = {(starting_pos.x, starting_pos.y)}
    
    def move(self, direction):
        for i in range(len(self.knots)):
            if i == 0:
                self.knots[i].move_direction(direction)
            else:
                self.knots[i].move(self.knots[i-1])
        
    def moves(self, move_vec):
        direction, scalar = move_vec_to_direction_scalar(move_vec)
        for _ in range(scalar):
            self.move(direction)
            self.tail_pos.add((self.knots[-1].x, self.knots[-1].y))

def parse_command(line):
    temp = line.split(" ")
    direction, step = temp[0], int(temp[1])

    if direction == "R":
        return Direction.RIGHT.value * step
    elif direction == "L":
        return Direction.LEFT.value * step
    elif direction == "U":
        return Direction.UP.value * step
    return Direction.DOWN.value * step

def find_start_pos_and_size(arr_moves):
    maxi_x, maxi_y, mini_x, mini_y = 0, 0, 0, 0
    current_pos = Vector(0, 0)
    
    for command in arr_moves:
        current_pos += command
        if current_pos.x < mini_x:
            mini_x = current_pos.x
        elif current_pos.x > maxi_x:
            maxi_x = current_pos.x
        
        if current_pos.y < mini_y:
            mini_y = current_pos.y
        elif current_pos.y > maxi_y:
            maxi_y = current_pos.y
    
    start_pos = Vector(-mini_x, -mini_y)
    return start_pos

def count_position_tail(starting_pos, arr_moves):    
    rope = Rope(starting_pos, 10)
    for move in arr_moves:
        rope.moves(move)
    
    return len(rope.tail_pos)

if __name__ == "__main__":
    lines = read_txt_file("input")
    arr_moves = list(map(lambda line : parse_command(strip(line)), lines))
    start_pos = find_start_pos_and_size(arr_moves)
    answer = count_position_tail(start_pos, arr_moves)
    print("Nb position the tail visited : ", answer)
    