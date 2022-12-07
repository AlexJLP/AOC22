from collections import defaultdict
from pathlib import Path

from aoc_session import get_input

inp = get_input(7).split("\n")

CWD = Path("/")
directory_sizes = defaultdict(int)

for line in inp:
    CWD = CWD.resolve()
    match line.split():
        case ['$', 'cd', '/']:
            CWD = Path("/")  # reset
        case ['$', 'cd', '..']:
            CWD = CWD / '..'
        case ['$', 'cd', destination]:
            CWD = CWD / destination
        case ['$', 'ls']:
            pass  # nothing to do on the input
        case ['dir', directory]:
            pass  # nothing to do on the input
        case [size, _] if size.isdigit():
            # seems like we actually don't care about the file .. increase directory
            for dir in [CWD, *CWD.parents]:
                directory_sizes[dir] += int(size)
        case _:
            raise ValueError

print(f"Part 1: {sum([v for v in directory_sizes.values() if v <= 100000])}")
# Can use size of fs / root to calc free up:
total_fs = directory_sizes[Path("/").resolve()]
p2 = min(
    [v for v in directory_sizes.values() if (total_fs - v) <= (70000000 - 30000000)]
)
print(f"Part 2: {p2}")
