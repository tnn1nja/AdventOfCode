#Output Grid to Console
def debugPrintGrid(grid):
    print("            -- GRID --")
    for l in grid:
        for i in l:
            print(f"{i}  ", end="")
        print("")
    print("")

#Boolean - is Coordinate on the Grid
def isValidCoord(coord0, coord1, grid):
    return (coord0 >= 0 and coord0 < len(grid) and\
            coord1 >= 0 and coord1 < len(grid[0]))

#Count Total Antinodes (#) on the Grid
def getAntinodeCount(grid):
    inital = 0
    other = 0
    for l in grid:
        for i in l:
            if i == "#":
                inital += 1
            elif i == "@":
                other += 1
    return inital, inital + other


#Read in Grid from File
grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid.append([char for char in line.rstrip("\n")])

#Extract Antenna Positions
antennas = {}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        symb = grid[i][j]
        if symb != ".":
            if symb in antennas:
                antennas[symb] = antennas.get(symb) + [[i, j]]
            else:
                antennas[symb] = [[i,j]]

#Find Antinodes
antinodes = []
for symb in antennas:
    coords = antennas.get(symb)
    for first in coords:
        for second in coords:
            if first != second:
                di, dj = first[0]-second[0], first[1]-second[1]
                test = [first[0] + di, first[1] + dj]
                grid[first[0]][first[1]] = "@"
                inital = True
                while isValidCoord(test[0], test[1], grid):
                    if inital:
                        grid[test[0]][test[1]] = "#"
                    else:
                        grid[test[0]][test[1]] = "@"
                    test = [test[0] + di, test[1] + dj]
                    inital = False
partOneAns, partTwoAns = getAntinodeCount(grid)

#Output
print(f"Part One Answer: {partOneAns}")
print(f"Part Two Answer: {partTwoAns}")