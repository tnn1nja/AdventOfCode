with open("2025/input.txt", "r") as f:
    grid = []
    for line in f.readlines():
        grid.append([])
        for char in line.rstrip("\n"):
            grid[-1].append(char == "@")

def is_paper_roll(i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
        return grid[i][j]
    return False

def can_be_removed(i, j):
    adjacent = -1
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            adjacent += is_paper_roll(i+di, j+dj)
            if adjacent == 4:
                return False
    return True

part_one = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if is_paper_roll(i, j):
            part_one += can_be_removed(i, j)

part_two = 0
contains_removeable = True
while contains_removeable:
    contains_removeable = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_paper_roll(i, j):
                if can_be_removed(i, j):
                    part_two += 1
                    contains_removeable = True
                    grid[i][j] = False

print(f"Part One Answer: {part_one}")
print(f"Part Two Answer: {part_two}")