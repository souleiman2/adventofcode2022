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
        vec = Vector(0,0)
        
        if self.x > next_knot.x:
            vec.x = 1
        elif self.x < next_knot.x:
            vec.x = -1
            
        if self.y > next_knot.y:
            vec.y = 1
        elif self.y < next_knot.y:
            vec.y = -1
            
        

class Rope:
    def __init__(self, pos):
        self.pos_tail = pos.clone()
        self.pos_head = pos.clone()
    
    def is_head_tail_touching(self):
        return 
    
    def move():
        pass
    
    def line_close(self, move_vec):
        arr_visited = []
        
        direction = None
        move_diag = False
        if move_vec.x == 0:
            if move_vec.y > 0:
                direction = Vector(0, 1)
            else:
                direction = Vector(0, -1)
            
            if self.pos_head.x != self.pos_tail.x:
                move_diag = True
            
        else:
            if move_vec.x > 0:
                direction = Vector(1, 0)
            else:
                direction = Vector(-1, 0)
            
            if self.pos_head.y != self.pos_tail.y:
                move_diag = True
        
        if move_diag:
            if direction.x == 0:
                # move vertical
                self.pos_tail = Vector(self.pos_head.x, self.pos_tail.y) + direction
            else:
                #move horizontal
                self.pos_tail = Vector(self.pos_tail.x, self.pos_head.y) + direction
            arr_visited.append(self.pos_tail.clone())
        
        while not self.is_head_tail_touching():
            self.pos_tail += direction
            arr_visited.append(self.pos_tail.clone())
        return arr_visited
    
    def move(self, move_vec):
        # first move of head
        self.pos_head += move_vec

        new_tail_position = []
        # movement of tail
        if not self.is_head_tail_touching():
            new_tail_position += self.line_close(move_vec)
            self.pos_tail = new_tail_position[-1]
        
        return new_tail_position

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
    size = Vector(maxi_x - mini_x + 1, maxi_y - mini_y + 1)
    
    return start_pos, size

def count_matrix(matrix):
    return sum(sum(elem) for elem in matrix)

def visited_pos(visited_matrix, positions):
    for pos in positions:
        visited_matrix[pos.y][pos.x] = True

def count_position_tail(size, starting_pos, arr_moves):
    bool_matrix = [[False for _ in range(size.x)] for _ in range(size.y)]
    visited_pos(bool_matrix, [starting_pos])
    
    rope = Rope(starting_pos)
    for move in arr_moves:
        tail_visited = rope.move(move)
        visited_pos(bool_matrix, tail_visited)
    
    return count_matrix(bool_matrix)


if __name__ == "__main__":
    lines = read_txt_file("input")
    arr_moves = list(map(lambda line : parse_command(strip(line)), lines))
    start_pos, size = find_start_pos_and_size(arr_moves)
    answer = count_position_tail(size, start_pos, arr_moves)
    print("Nb position the tail visited : ", answer)
    