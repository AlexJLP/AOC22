import numpy as np

from aoc_session import get_input

inp = get_input(9).split("\n")


vectors = {
    "U": np.array([-1, 0]),
    "D": np.array([1, 0]),
    "L": np.array([0, -1]),
    "R": np.array([0, 1]),
}

# Starting Position
head = np.array([0, 0])
tail = np.array([0, 0])
tail_history = {(0, 0)}


def calculate_tail_movement(h, t):
    distance = t - h
    if (abs(distance) <= np.array([1, 1])).all():
        # Adjacent. No move needed
        return np.array([0, 0])
    # If the head is ever two steps directly up, down, left, or right from the tail, the tail must
    # also move one step in that direction so it remains close enough:
    if (abs(distance) == [2, 0]).all():
        return np.array([-1 * np.sign(distance[0]), 0])
    elif (abs(distance) == [0, 2]).all():
        return np.array([0, -1 * np.sign(distance[1])])
    else:
        # Otherwise, if the head and tail aren't touching and aren't in the same row or column, the
        # tail always moves one step diagonally to keep up:
        return np.array([-1 * np.sign(distance[0]), -1 * np.sign(distance[1])])


for line in inp:
    move, moves = line.split(" ")
    for _ in range(int(moves)):
        # first move the head
        head += vectors[move]
        # then match the logic for the tail...
        tm = calculate_tail_movement(head, tail)
        tail += tm
        tail_history.add(tuple(tail))

print(f"Part 1: {len(tail_history)}")

###
head = np.array([0, 0])
tails = [np.array([0, 0]) for _ in range(9)]
tails_history = {(0, 0)}


for line in inp:
    move, moves = line.split(" ")
    for _ in range(int(moves)):
        head += vectors[move]
        # then match the logic for ALL TAILS
        predecessor = head
        for t in tails:
            tm = calculate_tail_movement(predecessor, t)
            t += tm
            predecessor = t
        tails_history.add(tuple(predecessor))
print(f"Part 2: {len(tails_history)}")
