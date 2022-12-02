from aoc_session import get_input
from enum import Enum


class MoveChoice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0


WIN_MAPPING = {
    MoveChoice.ROCK: MoveChoice.SCISSORS,
    MoveChoice.SCISSORS: MoveChoice.PAPER,
    MoveChoice.PAPER: MoveChoice.ROCK,
}

MOVE_MAPPING = {
    "A": MoveChoice.ROCK,
    "B": MoveChoice.PAPER,
    "C": MoveChoice.SCISSORS,
    "X": MoveChoice.ROCK,
    "Y": MoveChoice.PAPER,
    "Z": MoveChoice.SCISSORS,
    MoveChoice.ROCK: MoveChoice.ROCK,
    MoveChoice.PAPER: MoveChoice.PAPER,
    MoveChoice.SCISSORS: MoveChoice.SCISSORS,
}


def score(my_move, opponent_move):
    my_move = MOVE_MAPPING[my_move]
    opponent_move = MOVE_MAPPING[opponent_move]

    if my_move == opponent_move:
        return Outcome.DRAW.value + my_move.value
    elif WIN_MAPPING[my_move] == opponent_move:
        return Outcome.WIN.value + my_move.value
    else:
        return Outcome.LOSE.value + my_move.value


rounds = [r.split(" ") for r in get_input(2).split("\n")[:-1]]

print("Part1:")
print(sum(score(r[1], r[0]) for r in rounds))

###

LOSE_MAPPING = {v: k for k, v in WIN_MAPPING.items()}
OUTCOME_MAPPING = {"X": Outcome.LOSE, "Y": Outcome.DRAW, "Z": Outcome.WIN}


def get_move(desired_outcome, opponent_move):
    opponent_move = MOVE_MAPPING[opponent_move]
    desired_outcome = OUTCOME_MAPPING[desired_outcome]
    if desired_outcome == Outcome.DRAW:
        return opponent_move
    elif desired_outcome == Outcome.WIN:
        return LOSE_MAPPING[opponent_move]
    else:
        return WIN_MAPPING[opponent_move]


print("Part2:")
print(sum(score(get_move(r[1], r[0]), r[0]) for r in rounds))