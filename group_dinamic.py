def read_file():
    with open("input", "r") as file:
        # Read the first line of the file
        n_events, n_groups, n_turns = map(int, file.readline().split())

        # Read the event data
        events = []
        for i in range(n_events):
            event_turns = list(map(int, file.readline().split()))
            events.append(event_turns)

        # Read the group data
        groups = []
        preferences = []
        for i in range(n_groups):
            group_turns = list(map(int, file.readline().split()))
            groups.append(group_turns)

            group_preference = list(map(int, file.readline().split()))
            preferences.append(group_preference)

    return n_events, n_groups, n_turns, events, groups, preferences

def fill_grid(n, m, k):

    grid = [[-1 for _ in range(m)] for _ in range(n)]
    def backtrack(row, col):
        if row == n:
            return True
        for i in range(1, k+1):
            if i not in grid[row] and all(grid[r][col] != i for r in range(row)):
                grid[row][col] = i
                if col + 1 == m:
                    if backtrack(row + 1, 0):
                        return True
                else:
                    if backtrack(row, col + 1):
                        return True
                grid[row][col] = -1
        return False

    backtrack(0, 0)
    return grid

def print_grid(grid):

    for row in grid:
        for num in row:
            print(num, end=' ')
        print()

n_events, n_groups, n_turns, events, groups, preferences = read_file()
grid = fill_grid(n_turns, n_events, n_groups)

print("n_events:", n_events)
print("n_groups:", n_groups)
print("n_turns:", n_turns)
print("events:", events)
print("groups:", groups)
print("preferences:", preferences)

print_grid(grid)
