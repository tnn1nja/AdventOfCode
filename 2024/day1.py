#Parse Inputs
left = []
right = []
with open("input.txt", "r") as f:
    for line in f:
        parsed = line.rstrip("\n").split("   ")
        left.append(int(parsed[0]))
        right.append(int(parsed[1]))
left.sort()
right.sort()

#Part One
partOneAns = 0
for i in range(len(left)):
    partOneAns += abs(left[i]-right[i])

#Part Two
partTwoAns = 0
for num in left:
    partTwoAns += right.count(num)*num

#Output
print(f"Part One Ans: {partOneAns}")
print(f"Part Two Ans: {partTwoAns}")