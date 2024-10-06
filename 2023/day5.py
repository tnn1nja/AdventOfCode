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
def translateValue(value):
    for map in maps:
        value = mapValue(value, map)
    return value

#Calculate Part 1
partOneAns = 100000000000000000000000000
for value in values:
    newValue = translateValue(value)
    if newValue < partOneAns:
        partOneAns = newValue
print(f"Part 1 Answer: {partOneAns}")

#Calculate Part 2
partTwoAns = 100000000000000000000000000
for i in range(0, len(values), 2):
    for j in range(values[i+1]):
        newValue = translateValue(values[i]+j)
        if newValue < partTwoAns:
            partTwoAns = newValue
    print(f"Value Range Complete, Current Minimum: {partTwoAns}")
print(f"Part 2 Answer: {partTwoAns}")