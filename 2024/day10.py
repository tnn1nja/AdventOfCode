#Determine if Coord is on Grid
def isValidCoord(grid, altCoord):
    return (altCoord[0] >= 0 and altCoord[0] < len(grid) and\
            altCoord[1] >= 0 and altCoord[1] < len(grid[0]))

#Recursive Trail Counter
def getTrails(grid, coord, endPoints = None, totalRoutes = 0):
    if endPoints == None:
        endPoints = set()
    for i in range(-1, 2):
        if i == 0:
            spread = range(-1, 2) 
        else:
            spread = range(0, 1)
        for j in spread:
            altCoord = [coord[0]+i, coord[1]+j]
            if isValidCoord(grid, altCoord):
                if grid[altCoord[0]][altCoord[1]] == grid[coord[0]][coord[1]]+1:
                    if grid[altCoord[0]][altCoord[1]] == 9:
                        totalRoutes += 1
                        endPoints.add((altCoord[0], altCoord[1]))
                    else:
                        trails = getTrails(grid, altCoord)
                        totalRoutes += trails[1]
                        endPoints.update(trails[0])
    return endPoints, totalRoutes

#Read in Grid from File
grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid+= [[int(char) for char in line.rstrip("\n")]]

#Calculate
partOneAns = 0
partTwoAns = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            trails = getTrails(grid, [i,j])
            partOneAns += len(trails[0])
            partTwoAns += trails[1]

#Output
print(f"Part One Answer: {partOneAns}")
print(f"Part Two Answer: {partTwoAns}")