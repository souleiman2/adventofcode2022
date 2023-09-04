import sys
sys.path.append('..') # to be able to import files from parent directory
from .. import utils

from enum import Enum

class OwnShape(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"
    
class OppShape(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

def calc_score_shape(shape):
    if shape == "X":
        return 1
    elif shape == "Y":
        return 2
    elif shape == "Z":
        return 3
    raise ValueError("The shape should only be either X, Y or Z")

def calc_score_win(own_shape, opp_shape):
    if (own_shape == OwnShape.ROCK.value and opp_shape == OppShape.SCISSORS.value) or \
        (own_shape == OwnShape.SCISSORS.value and opp_shape == OppShape.PAPER.value) or \
        (own_shape == OwnShape.PAPER.value and opp_shape == OppShape.ROCK.value):
            return 6
    elif (own_shape == OwnShape.ROCK.value and opp_shape == OppShape.ROCK.value) or \
        (own_shape == OwnShape.PAPER.value and opp_shape == OppShape.PAPER.value) or \
        (own_shape == OwnShape.SCISSORS.value and opp_shape == OppShape.SCISSORS.value):
            return 3
    return 0
        

def calc_score_round(line):
    temp = line.split(" ")
    opp_shape, own_shape = temp
    shape_score = calc_score_shape(own_shape)
    win_score = calc_score_win(own_shape, opp_shape)
    return win_score + shape_score

if __name__ == "__main__":
    lines = utils.read_txt_file("input")
    lines = list(map(utils.strip, lines))
    scores = list(map(calc_score_round, lines))
    print(f"Total score : {sum(scores)}")