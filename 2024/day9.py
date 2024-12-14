from copy import deepcopy

#Parse Disk from File
def getDiskFromFile(filename):
    disk = []
    with open(filename, "r") as file:
        inputNums = file.read()
    for i in range(len(inputNums)):
        if (i % 2 == 0):
            temp = [i//2, int(inputNums[i])]
            if temp[1] > 0:
                disk += [temp]
        else:
            temp = [-1, int(inputNums[i])]
            if temp[1] > 0:
                disk += [temp]
    return disk

#Find Part One Answer
def getFragCheckSum(fragDisk):
    count = 0
    for i in range(len(fragDisk)):
        if fragDisk[i] != -1:
            count += i*fragDisk[i]
    return count

#Find Part Two Answer
def getDefragCheckSum(defragDisk):
    fragDisk = []
    for pair in defragDisk:
        for i in range(pair[1]):
            fragDisk.append(pair[0])
    return getFragCheckSum(fragDisk)

#Index of Next Individual Space
def getNextFragSpace(disk, index):
    for i in range(index+1, len(disk)):
        if disk[i] == -1:
            return i
    return -2

#Sort Disk for Part One
def sortDiskFrag(disk):
    fragDisk = []
    for file in disk:
        fragDisk += [file[0]]*file[1]

    index = len(fragDisk)-1
    nextSpace = getNextFragSpace(fragDisk, 0)
    while nextSpace != -2 and nextSpace < len(fragDisk)-1:
        if fragDisk[index] != -1:
            fragDisk[nextSpace] = fragDisk[index]
            nextSpace = getNextFragSpace(fragDisk, nextSpace)
        fragDisk.pop(index)
        index -= 1

    return fragDisk

#Sort Disk for Part Two
def sortDiskDefrag(disk):
    defragDisk = deepcopy(disk)
    index = (len(defragDisk))-1
    while index > -1:
        if defragDisk[index][0] != -1:
            nextSpace = 0
            moved = False
            while nextSpace < index and not moved:
                if defragDisk[nextSpace][0] == -1 and\
                    defragDisk[index][1] <= defragDisk[nextSpace][1]:
                    defragDisk[nextSpace][1] = \
                        defragDisk[nextSpace][1] - defragDisk[index][1]
                    defragDisk.insert(nextSpace, deepcopy(defragDisk[index]))
                    defragDisk[index+1][0] = -1
                    if defragDisk[index][0] == -1:
                        defragDisk[index+1][1] += defragDisk[index][1]
                        defragDisk[index][1] = 0
                    if index+2 < len(defragDisk)-1 and defragDisk[index+2][0] == -1:
                        defragDisk[index+1][1] += defragDisk[index+2][1]
                        defragDisk[index+2][1] = 0
                    index += 2
                    moved = True
                nextSpace +=1
        index -= 1

    return defragDisk

#Run and Output
disk = getDiskFromFile("input.txt")
print(f"Part One Answer: {getFragCheckSum(sortDiskFrag(disk))}")
print(f"Part Two Answer: {getDefragCheckSum(sortDiskDefrag(disk))}")