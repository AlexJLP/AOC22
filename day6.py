from aoc_session import get_input

inp = get_input(6).strip()

def find_position(input_string, marker_length, position=0):
    while position + marker_length < len(input_string):
        current = set(input_string[position:position+marker_length])
        if len(current) == marker_length:
            return position + marker_length
        position += 1
    # Exhausted the input :(
    raise ValueError


print(f"Part 1: {find_position(inp, 4)}")
print(f"Part 2: {find_position(inp, 14)}")
