def doCalc(calc):
    operands = calc[:-1]
    if "+" in calc[-1]:
        total = 0
        for operand in operands:
            total += int(operand)
    else:
        total = 1
        for operand in operands:
            total *= int(operand)
    return total

with open("input.txt", "r") as f:
    lines = f.readlines()

#Part 1
sums = [[]]
for collumn in range(len(lines[0])-1):
    only_spaces = True
    for row in range(len(lines)):
        char = lines[row][collumn]
        if char != " ": 
            only_spaces = False
        if len(sums[-1]) > row:
            sums[-1][row] += char
        else:
            sums[-1].append(char)
    if only_spaces:
        sums[-1] = [x[:-1] for x in sums[-1]]
        sums.append([])

part_one = 0
for s in sums:
    part_one += doCalc(s)

#Part 2
for i in range(len(sums)):
    new_sum = []
    for j in range(len(sums[i][0])):
        num = ""
        for n in sums[i][:-1]:
            num += n[j]
        new_sum.append(num)
    new_sum.append(sums[i][-1])
    sums[i] = new_sum

part_two = 0
for s in sums:
    part_two += doCalc(s)


#Output
print(f"Part One Answer: {part_one}")
print(f"Part Two Answer: {part_two}")