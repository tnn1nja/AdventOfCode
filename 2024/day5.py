#Parse Text Files
key = {}
printOrders = []
with open("input.txt", "r") as f:
    readingKey = True
    for line in f:
        if line == "\n":
            readingKey = False
        else:
            if readingKey:
                data = [int(x) for x in line.strip("\n").split("|")]
                if data[1] in key:
                    key[data[1]] = key.get(data[1]) + [data[0]]
                else:
                    key[data[1]] = [data[0]]
            else:
                printOrders.append([int(x) for x in line.strip("\n").split(",")])

#Find if Print Order is Valid
def isValidOrder(order):
    for i in range(len(order)):
        num = order[i]
        if (num in key):
            for value in key.get(num):
                if value in order and value not in order[:i]:
                    return False
    return True

#Find Minimum Safe Index for Element
def getMinSafeIndex(index, arr):
    num = arr[index]

    minSafeIndex = 0
    for value in key.get(num):
        if value in arr and arr.index(value) > minSafeIndex:
            minSafeIndex = arr.index(value)

    return minSafeIndex

#Sort Print Order
def sortOrder(pOrder):
    printOrder = pOrder.copy()
    for i in range(len(printOrder)-1, -1, -1):
        if printOrder[i] in key:
            printOrder.insert(getMinSafeIndex(i, printOrder), printOrder.pop(i))
    if isValidOrder(printOrder):
        return printOrder
    else:
        return sortOrder(printOrder)

#Find Middle Item in Array
def getMiddleItem(arr):
    return arr[len(arr)//2]

#Run
partOneAns = 0
partTwoAns = 0
for printOrder in printOrders:
    if isValidOrder(printOrder):
        partOneAns += getMiddleItem(printOrder)
    else:
        partTwoAns += getMiddleItem(sortOrder(printOrder))

#Output
print(f"Part One Answer: {partOneAns}")
print(f"Part Two Answer: {partTwoAns}")