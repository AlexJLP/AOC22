import itertools
from io import StringIO
import numpy as np

from aoc_session import get_input

inp = StringIO(get_input(8))
# Parse into numpy array
arr = np.genfromtxt(inp, dtype="int", delimiter=1)
print(arr)


def visibility(row, col, x, y, value):
    if x == 0 or y == 0 or x == len(col) - 1 or y == len(row) - 1:
        # on edge, always visible, but no viewing score cause 0 trees in at least one direction
        return True, 0
    print(f"{row},{col},{x},{y} -> {value}")
    if value != row[y] or value != col[x]:
        # Sanity check for myself...
        raise ValueError
    # Parse out s
    row_left = row[:y]
    row_right = row[y + 1 :]
    col_top = col[:x]
    col_bot = col[x + 1 :]
    # Visibility scores
    def viz_helper(l):
        trees_so_far = 0
        for tree in l:
            trees_so_far += 1
            if tree >= value:
                break
        return trees_so_far
    # Flip left and top, as we go backwards for visibility purposes.
    left_viz_score = viz_helper(np.flipud(row_left))
    right_viz_score = viz_helper(row_right)
    up_viz_score = viz_helper(np.flipud(col_top))
    down_viz_score = viz_helper(col_bot)
    return (
        max(row_left) < value
        or max(row_right) < value
        or max(col_top) < value
        or max(col_bot) < value,
        left_viz_score * right_viz_score * up_viz_score * down_viz_score,
    )


(cols, rows) = arr.shape
visible = []
viewing_score = []

for x, y in itertools.product(range(rows), range(cols)):
    row = arr[[x], :].ravel()
    column = arr[:, [y]].ravel()
    (is_visible, viz_score) = visibility(row, column, x, y, arr[x][y])
    visible.append(is_visible)
    viewing_score.append(viz_score)

print(f"Part 1: {sum(visible)}")
print(f"Part 2: {max(viewing_score)}")
