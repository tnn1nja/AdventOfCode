f = open("test.txt", "r")
lines = f.readlines()
f.close()

def onlyZeros(inpArr):
    for value in inpArr:
        if value != 0:
            return False
    return True

def findLowerArr(inpArr):
    output = []
    for i in range(len(inpArr)-1):
        output.append(inpArr[i+1] - inpArr[i])
    return output

def getNextValue(inpArr):
    nextValue = 0
    while not onlyZeros(inpArr):
        nextValue += inpArr[-1]
        inpArr = findLowerArr(inpArr)

    return nextValue

def getPrevValue(inpArr):
    prevValue = 0
    while not onlyZeros(inpArr):
        prevValue += inpArr[0]
        inpArr = findLowerArr(inpArr)

    return prevValue

partOneAns = 0
for line in lines:
    temp = line.rstrip().split(" ")
    partOneAns += getNextValue([int(x) for x in temp])
print(f"Part 1 Answer: {partOneAns}")

partTwoAns = 0
for line in lines:
    temp = line.rstrip().split(" ")
    temp2 = getPrevValue([int(x) for x in temp])
    partTwoAns += temp2
print(f"Part 2 Answer: {partTwoAns}")