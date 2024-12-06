def read_file(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.readlines()
    return [list(line.strip()) for line in content] 


def find_guard(map, guard):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == guard:
                return i, j
    return None


def turn_right(guard):
    turns = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^'
    }
    return turns[guard]


def predict_path(map):
    guard = '^'
    position = find_guard(map, guard)
    if position is None:
        raise ValueError("Guard not found in the map")

    visited = set()
    
    directions = {
        '^': (-1, 0),  # up
        '>': (0, 1),   # right
        'v': (1, 0),   # down
        '<': (0, -1)   # left
    }
    
    out_of_map = False
    rows, cols = len(map), len(map[0])

    while not out_of_map:
        move = directions[guard]
        next_position = (position[0] + move[0], position[1] + move[1])
        # Check if the guard is out of the map
        if (
            next_position[0] < 0 or next_position[0] >= rows or
            next_position[1] < 0 or next_position[1] >= cols
        ):
            out_of_map = True

        # Check for an obstacle
        if map[next_position[0]][next_position[1]] == '#':
            guard = turn_right(guard)
        else:
            # update the guards position
            position = next_position
            visited.add(position)

    return len(visited)


# Part one
filename = "day6input.txt"
map = read_file(filename)
print(f"The guard will visit {predict_path(map)} distinct positions before leaving the area")
# Part two
