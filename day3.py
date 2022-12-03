from aoc_session import get_input

backpacks = get_input(3).split("\n")


def priority(letter):
    return ord(letter) - 38 if ord(letter) <= 90 else ord(letter) - 96


priority_sum = sum(
    priority(
        (
            set(backpack[: len(backpack) // 2]) & set(backpack[len(backpack) // 2 :])
        ).pop()
    )
    for backpack in backpacks
)


print("Part 1")
print(priority_sum)

###

badge_sum = sum(
    priority(set.intersection(*map(set, group)).pop())
    for group in (backpacks[i : i + 3] for i in range(0, len(backpacks), 3))
)
print("Part 2")
print(badge_sum)
