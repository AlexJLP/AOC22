import pandas as pd
from aoc_session import get_input

inp = get_input(10).split("\n")

x_register = 1
cpu_cycle = 1
register_history = pd.DataFrame(columns=["x_register"])

for line in inp:
    match line.split(" "):
        case ["noop"]:
            cpu_cycle += 1
        case "addx", value:
            cpu_cycle += 2
            x_register += int(value)
        case _:
            print(f"Unknown: '{line}'")
    register_history.loc[cpu_cycle] = x_register

# Fill in missing cycles
register_history = (
    register_history.reindex(pd.RangeIndex(register_history.index.max() + 1))
    .ffill()
    .fillna(1)
)

print(
    f"Part 1: {sum(cycle * register_history.loc[cycle]['x_register'] for cycle in range(20,221,40))}"
)

###
def draw(cycle, x_reg):
    sprite_pos = 41 * [" "]
    sprite_pos[x_reg - 1 : x_reg + 2] = 3 * ["#"]
    print(sprite_pos[cycle % 40 - 1], end="")


print("Part 2: ")
for cycle, (index, row) in enumerate(register_history.iterrows()):
    if cycle == 0:
        continue
    draw(cycle, int(row["x_register"]))
    if (cycle % 40) == 0:
        print()
