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

#Index of Next Individual Space
def getNextFragSpace(disk, index):
    for i in range(index+1, len(disk)):
        if disk[i] == -1:
            return i
    return -2

#Find Final Answer
def getCheckSum(disk):
    count = 0
    for i in range(len(disk)):
        if disk[i] != -1:
            count += i*disk[i]
    return count

#Sort Disk for Part One
def sortDiskFrag(disk):
    fragDisk = []
    for file in disk:
        fragDisk += [file[0]]*file[1]

    index = len(fragDisk)-1
    nextFreeSpace = getNextFragSpace(fragDisk, 0)
    while nextFreeSpace != -2 and nextFreeSpace < len(fragDisk)-1:
        if fragDisk[index] != -1:
            fragDisk[nextFreeSpace] = fragDisk[index]
            nextFreeSpace = getNextFragSpace(fragDisk, nextFreeSpace)
        fragDisk.pop(index)
        index -= 1

    return fragDisk

#Sort Disk for Part Two
def sortDiskDefrag(disk):
    defragDisk = deepcopy(disk)


#Run and Output
disk = getDiskFromFile("test.txt")
print(disk)
print(f"Part One Answer: {getCheckSum(sortDiskFrag(disk))}")
sortDiskDefrag(disk)