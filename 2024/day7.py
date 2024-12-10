#Find if Part One is Possible
def isPossiblePartOne(values):
    for i in range(2**(len(values)-2)):
        perm = bin(i)[2:].zfill(len(values)-2)
        total = values[1]
        for j in range(2,len(values)):
            if perm[j-2] == "0":
                total += values[j]
            else:
                total *= values[j]
        if total == values[0]:
            return values[0]
    return False

#Convert Denary to Ternary
def denaryToTernary(denary):
    if denary < 3:
        output = str(denary)
    else:
        output = ""
        while denary > 0:
            output = str(denary % 3) + output
            denary = denary//3
    return output

#Find if Part Two is Possible
def isPossiblePartTwo(values):
    for i in range(3**(len(values)-2)):
        perm = denaryToTernary(i).zfill(len(values)-2)
        total = values[1]
        for j in range(2, len(values)):
            if perm[j-2] == "0":
                total += values[j]
            elif perm[j-2] == "1":
                total *= values[j]
            else:
                total = int(f"{total}{values[j]}")
        if total == values[0]:
            return values[0]
    return 

#Calculate Answers
partOneAns = 0
partTwoAns = 0
with open("input.txt", "r") as file:
    for line in file:
        values = [int(x) for x in line.rstrip("\n").replace(":", "").split(" ")]
        partTwoResult = isPossiblePartTwo(values)
        if partTwoResult:
            partTwoAns += partTwoResult
            partOneResult = isPossiblePartOne(values)
            if partOneResult:
                partOneAns += partOneResult

#Output
print(f"Part One Answer: {partOneAns}")
print(f"Part Two Answer: {partTwoAns}")