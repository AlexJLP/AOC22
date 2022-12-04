import itertools
from aoc_session import get_input

pairs = get_input(4).split("\n")

assignments = [
    list(
        itertools.starmap(
            lambda a, b: set(range(a, b + 1)),
            [map(int, a.split("-")) for a in pair.split("," "")],
        )
    )
    for pair in pairs
]

fully_contained = filter(
    lambda x: x[0].issubset(x[1]) or x[1].issubset(x[0]), assignments
)

print("Part1:")
print(len(list(fully_contained)))

###

overlapping = filter(lambda x: x[0] & x[1], assignments)

print("Part2:")
print(len(list(overlapping)))
