import re

def doCalc(calc):
    operands = calc[:-1]
    if calc[-1] == "+":
        total = 0
        for operand in operands:
            total += int(operand)
    else:
        total = 1
        for operand in operands:
            total *= int(operand)
    return total

with open("test.txt", "r") as f:
    lines = f.readlines()

part_one_sums = []
s = [[] for x in lines]
for collumn in range(len(lines[0])-1):
    only_spaces = True
    for row in range(len(lines)):
        if lines[row][collumn] != " ":
            only_spaces = False
        s[row].append(lines[row][collumn])
    if only_spaces:
        part_one_sums.append(s)
        s = [[] for x in lines]

print(part_one_sums)

"""
part_one = 0
for s in part_one_sums:
    part_one += doCalc(s)

print(f"Part One Answer: {part_one}")
"""