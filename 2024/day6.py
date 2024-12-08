from copy import deepcopy
from math import floor

#Output Grid to Console
def debugPrintGrid(grid):
    print("         -- GRID --")
    for l in grid:
        for i in l:
            print(f"{i}  ", end="")
        print("")
    print("")

#Find Number of Positions ('X') on Grid
def getDistinctPositions(grid):
    count = 0
    for l in grid:
        for i in l:
            if i == "X":
                count += 1
    return count

#Boolean - is Coordinate on the Grid
def isValidCoord(coord0, coord1, grid):
    return (coord0 >= 0 and coord0 < len(grid) and\
            coord1 >= 0 and coord1 < len(grid[0]))

#Moves the Guard Forward one Space
def moveGuard(pos, grid):
    di = 0
    dj = 0
    if pos[2] == 0:
        di = -1
    elif pos[2] == 1:
        dj = 1
    elif pos[2] == 2:
        di = 1
    else:
        dj = -1

    if not isValidCoord(pos[0]+di, pos[1]+dj, grid):
        return (False, grid)
    elif grid[pos[0]+di][pos[1]+dj] == "#":
        return moveGuard([pos[0],pos[1], (pos[2]+1)%4], grid)
    else:
        grid[pos[0]+di][pos[1]+dj] = "X"
        return ([pos[0]+di, pos[1]+dj, pos[2]], grid)

#Find Guards Initial Position
def getInitialGuardPos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                grid[i][j] = "X"
                return [i,j, 0], grid

#Determines if a Grid Layout will Loop 
def willLoop(grid):
    previousPositions = []
    guardPos, grid = getInitialGuardPos(grid)
    while guardPos and guardPos not in previousPositions:
        previousPositions += [guardPos]
        guardPos, grid = moveGuard(guardPos, grid)
    return guardPos


#Read in Grid From File
cleanGrid = []
with open("day6.txt", "r") as f:
    for l in f:
        cleanGrid.append([x for x in l.rstrip("\n")])

#Process Part One Moves
guardPos, grid = getInitialGuardPos(deepcopy(cleanGrid))
while guardPos:
    guardPos, grid = moveGuard(guardPos, grid)
partOneAns = getDistinctPositions(grid)
print("Part One Complete")

#Process Part Two
partTwoAns = 0
for i in range(len(cleanGrid)):
    for j in range(len(cleanGrid[0])):
        grid = deepcopy(cleanGrid)
        if grid[i][j] == ".":
            grid[i][j] = "#"
            if willLoop(grid):
                partTwoAns += 1
    print(f"Part Two Progress: {floor((i+1)/len(cleanGrid)*100)}%")
print("Part Two Complete")

#Output Answers
print("\nAnswers:")
print(f"Part One Answer: {partOneAns}") #5153
print(f"Part Two Answer: {partTwoAns}") #1711