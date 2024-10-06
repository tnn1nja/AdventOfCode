from copy import deepcopy

#Read in File
f = open("input.txt", "r")
lines = f.readlines()
f.close()

#Extract Seed Values
values = lines[0].replace("\n", "").split(": ", 1)[1].split(" ")
for i in range(len(values)):
    values[i] = int(values[i])
    
#Extract Maps
maps = []
mapLines = lines[2:]
temp = []
for line in mapLines:
    if line[0].isdigit():
        tempBuilder = line.replace("\n", "").split(" ")
        for i in range(len(tempBuilder)):
            tempBuilder[i] = int(tempBuilder[i])
        temp.append(tempBuilder)
    elif line[0].isalpha():
        temp = []
    else:
        maps.append(temp)
maps.append(temp)

#Remapping Function
def mapValue(value, map):
    for field in map:
        distance = value - field[1]
        if distance >= 0 and distance < field[2]:
            return field[0] + distance
    return value

#Find Minimum Mapped Value
def findMinMapped(inpValues):
    mapsCompleted = 1
    for map in maps:
        for i in range(len(inpValues)):
            inpValues[i] = mapValue(inpValues[i], map)
        print(f"Map Completed ({mapsCompleted}/7)")
        mapsCompleted += 1
    return min(inpValues)

#Calculate Part 1
partOneAns = findMinMapped(deepcopy(values))
print(f"Part 1 Answer: {partOneAns}")

#Calculate Part 2
rangeValues = []
for i in range(0, len(values), 2):
    for j in range(values[i+1]):
        rangeValues.append(values[i]+j)
partTwoAns = findMinMapped(rangeValues)
print(f"Part 2 Answer: {partTwoAns}")
