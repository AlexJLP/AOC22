from aoc_session import get_input

elves = get_input(1).split("\n\n")
elves_calories = []
for elf in elves:
    elf_carry = map(int, elf.split("\n"))
    elves_calories.append(sum(list(elf_carry)))

print("Part1:")
print(max(elves_calories))  # top elf

###

print("Part2:")
print(sum(sorted(elves_calories)[-3:]))  # top 3
