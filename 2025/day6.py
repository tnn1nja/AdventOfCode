import re

part_one_sums = []
part_two_sums = []
with open("test.txt", "r") as f:
    for line_no, line in enumerate(f):
        line = re.sub(r" +", " ", line.strip()).split(" ")
        line = [int(x) if x.isdigit() else x for x in line]
        for i in range(len(line)):
            if len(part_one_sums) > i:
                part_one_sums[i].append(line[i])
            else:
                part_one_sums.append([line[i]])

def doCalc(calc):
    operands = calc[:-1]
    if calc[-1] == "+":
        total = 0
        for operand in operands:
            total += operand
    else:
        total = 1
        for operand in operands:
            total *= operand
    return total

part_one = 0
for s in part_one_sums:
    part_one += doCalc(s)

print(f"Part One Answer: {part_one}")