from pathlib import Path

# Open the file and read the lines, convert the lines in a list of characters
def read_file(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.readlines()
    return [list(line.strip()) for line in content] 

# Having the map, find the position of the guard
def find_guard(map, guard):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == guard:
                return i, j
    return None

# We have 2 instructions to follow, to take steps or to turn right when the guard finds an obstacle. This function turns right for all the possibilities the guard can find.
def turn_right(guard):
    turns = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^'
    }
    return turns[guard]

#  here we have a mix between part 1 and part 2
def predict_path(map, find_loop=False, obstacle_position=None):
    # If we are in "find_loop" mode and an obstacle position is provided,
    # we temporarily place an obstacle in that cell. This allows us to check
    # if adding this new obstacle causes the guard to enter a loop.
    if find_loop and obstacle_position is not None:
        # Store the original character before placing the obstacle
        r_ob, c_ob = obstacle_position
        original_char = map[r_ob][c_ob]
        # Temporarily replace that cell with an obstacle
        map[r_ob][c_ob] = '#'
        # This set will keep track of states (position + direction) to detect loops
        visited_states = set()

    # The guard always starts facing up ('^'). We find the guard's initial position.
    guard = '^'
    position = find_guard(map, guard)

    # Keep track of all visited positions. We add the initial position so that
    # it counts towards the total visited cells.
    visited = set()
    visited.add(position)

    # Define the movement vectors for each direction the guard might face.
    # For example, '^' means move one cell up in terms of the row index.
    directions = {
        '^': (-1, 0),  # Up: move one cell upwards
        '>': (0, 1),   # Right: move one cell to the right
        'v': (1, 0),   # Down: move one cell downwards
        '<': (0, -1)   # Left: move one cell to the left
    }

    # out_of_map will become True when the guard steps outside the boundaries of the map
    out_of_map = False
    rows, cols = len(map), len(map[0])

    # Main loop: runs until the guard leaves the map or we detect a loop (if we're checking for loops)
    while not out_of_map:
        # If we are checking for loops (find_loop is True and we have an obstacle_position),
        # we record the current state: the current position and the guard's direction.
        # If we encounter the same state again, it means the guard is stuck in a cycle.
        if find_loop and obstacle_position is not None:
            state = (position, guard)
            if state in visited_states:
                # We've seen this exact state before => a loop is detected
                # Restore the original map cell
                map[r_ob][c_ob] = original_char
                # Return None to indicate that a loop has been found
                return None
            visited_states.add(state)

        # Determine the guard's next position based on the current direction
        move = directions[guard]
        next_position = (position[0] + move[0], position[1] + move[1])

        # Check if the next position is outside the map boundaries
        if (
            next_position[0] < 0 or next_position[0] >= rows or
            next_position[1] < 0 or next_position[1] >= cols
        ):
            # The guard is about to step outside the map, so we stop
            out_of_map = True
        else:
            # If not outside, check if the next position contains an obstacle
            if map[next_position[0]][next_position[1]] == '#':
                # If there's an obstacle ahead, the guard turns right
                # and does not move forward this turn
                guard = turn_right(guard)
            else:
                # If there's no obstacle, the guard moves to the next cell
                position = next_position
                visited.add(position)  # Mark this new cell as visited

    # If we placed a temporary obstacle, we restore the original character before returning
    if find_loop and obstacle_position is not None:
        map[r_ob][c_ob] = original_char

    # If no loop was found or we're not checking for loops, we return the set of visited positions.
    # This set tells us how many distinct cells the guard visited before leaving the map.
    return visited

# Part one
script_dir = Path(__file__).parent
filename = script_dir / "day6input.txt"

map = read_file(filename)
visited_positions = predict_path(map)
print(f"The guard will visit {len(visited_positions)} distinct positions before leaving the area")

# Part two
initial_guard_position = find_guard(map, '^')
rows, cols = len(map), len(map[0])
loop_positions = []

for i in range(rows):
    for j in range(cols):
        if (i, j) == initial_guard_position:
            continue
        if map[i][j] == '.':
            result = predict_path(map, True,(i, j))
            if result is None:
                loop_positions.append((i, j))

print(f"There are {len(loop_positions)} positions where placing an obstruction would cause a loop")
