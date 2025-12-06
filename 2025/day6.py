with open("input.txt", "r") as f:
    lines = f.readlines()

part_one_sums = [[]]
for collumn in range(len(lines[0])-1):
    only_spaces = True
    for row in range(len(lines)):
        char = lines[row][collumn]
        if char != " ": 
            only_spaces = False
        if len(part_one_sums[-1]) > row:
            part_one_sums[-1][row] += char
        else:
            part_one_sums[-1].append(char)
    if only_spaces:
        part_one_sums[-1] = [x[:-1] for x in part_one_sums[-1]]
        part_one_sums.append([])

part_two_sums = []
for old_sum in part_one_sums:
    new_sum = []
    for i in range(len(old_sum[0])):
        num = ""
        for n in old_sum[:-1]:
            num += n[i]
        new_sum.append(num)
    new_sum.append(old_sum[-1])
    part_two_sums.append(new_sum)

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

part_one = 0
for s in part_one_sums:
    part_one += doCalc(s)

part_two = 0
for s in part_two_sums:
    part_two += doCalc(s)

print(f"Part One Answer: {part_one}")
print(f"Part Two Answer: {part_two}")