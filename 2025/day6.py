calcs = [[]]
with open("input.txt", "r") as f:
    lines = f.readlines()
    for collumn in range(len(lines[0])-1):
        only_spaces = True
        for row in range(len(lines)):
            char = lines[row][collumn]
            if char != " ": 
                only_spaces = False
            if len(calcs[-1]) > row:
                calcs[-1][row] += char
            else:
                calcs[-1].append(char)
        if only_spaces:
            calcs[-1] = [x[:-1] for x in calcs[-1]]
            calcs.append([])

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
part_two = 0
for calc in calcs:
    part_one += doCalc(calc)
    new = []
    for i in range(len(calc[0])):
        new_num = ""
        for old_num in calc[:-1]:
            new_num += old_num[i]
        new.append(new_num)
    new.append(calc[-1])
    part_two += doCalc(new)

print(f"Part One Answer: {part_one}")
print(f"Part Two Answer: {part_two}")