import copy
import re
import numpy as np
from aoc_session import get_input


inp = get_input(5).split("\n")
all_stacks = np.transpose(list(map(list, inp[: inp.index("") - 1])))
indexes = range(1, len(all_stacks), 4)

stacks = [
    list(stack[::-1]) for stack in ["".join(all_stacks[i]).strip() for i in indexes]
]
stacks_p2 = copy.deepcopy(stacks)

move_regex = re.compile(r"move (?P<count>\d+) from (?P<from>\d+) to (?P<to>\d+)")

for line in inp[inp.index("") + 1 :]:
    instruction = move_regex.search(line)
    count, to, fro = (
        int(instruction["count"]),
        int(instruction["to"]) - 1,
        int(instruction["from"]) - 1,
    )
    # Part 1
    for _ in range(count):
        stacks[to].append(stacks[fro].pop())
    # Part 2
    stacks_p2[to] += stacks_p2[fro][-count:]
    stacks_p2[fro] = stacks_p2[fro][:-count]


print(f"Part 1: {''.join([s[-1] for s in stacks])}")
print(f"Part 2: {''.join([s[-1] for s in stacks_p2 if len(s) > 0])}")
