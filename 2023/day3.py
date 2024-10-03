#Read File
f = open("input.txt", "r")
schem = f.readlines()
f.close()

#Remove \n
for i in range(len(schem)):
    schem[i] = schem[i].replace("\n", "")

#Find Adjacent Numbers
gearCoords = []
adjNums = []
for i in range(len(schem)-1):
    for j in range(len(schem[i])):
        if (not schem[i][j].isdigit()) and schem[i][j] != ".":
            for iMod in range(-1,2):
                for jMod in range(-1,2):
                    if schem[i+iMod][j+jMod].isdigit():
                        adjNums.append([i+iMod, j+jMod])
        if schem[i][j] == "*":
            gearCoords.append([i, j])

#Find Number Coord Origins
originCoords = []
for coord in adjNums:
    index = coord[1]
    try:
        while schem[coord[0]][index].isdigit():
            index-=1
        index+=1
    except:
        pass
    if [coord[0], index] not in originCoords:
        originCoords.append([coord[0], index])

#Find Full Numbers and Hitboxes
numData = []
for coord in originCoords:
    num = ""
    index = coord[1]
    try:
        while schem[coord[0]][index].isdigit():
            num+=schem[coord[0]][index]
            index+=1
    except:
        pass
    numData.append([coord[0], coord[1], len(num), int(num)])

#Calculate Part One
partOneAns = 0
for num in numData:
    partOneAns += num[3]
print(f"Part 1 Answer: {partOneAns}")

#Find Gear Powers
partTwoAns = 0
for coord in gearCoords:
    gearRatio = 1
    gearNums = 0
    for num in numData:
        if abs(num[0] - coord[0]) < 2:
            if (abs((num[1] + num[2]-1) - coord[1]) < 2) or (abs((num[1]) - coord[1]) < 2):
                gearRatio *= num[3]
                gearNums += 1
    if gearNums == 2:
        partTwoAns += gearRatio
print(f"Part Two Answer: {partTwoAns}")