#Calculate if a report is valid (Part 1 & 2)
def isValidReport(report, allowRecursion):
    growing = report[0] < report[1]
    for i in range(len(report)-1):
        diff = abs(report[i]-report[i+1])
        if not ((report[i] < report[i+1]) == growing 
                and diff < 4 and diff > 0):
            if allowRecursion:
                return isValidReport(stripIndex(report, i), False) or\
                      isValidReport(stripIndex(report, i+1), False) or\
                          (i == 1 and isValidReport(stripIndex(report, 0), False))
            else:
                return False
    return True

#Copy list without index
def stripIndex(list, index):
    output = list.copy()
    output.pop(index)
    return output

#Read in file and run
partOneAns = 0
partTwoAns = 0
with open("input.txt", "r") as file:
    for line in file:
        report = list(map(int, line.rstrip("\n").split(" ")))
        if isValidReport(report, False):
            partOneAns += 1
            partTwoAns += 1
        elif isValidReport(report, True):
            partTwoAns += 1

#Output
print(f"Part One Answer: {partOneAns}")
print(f"Part Two Answer: {partTwoAns}")