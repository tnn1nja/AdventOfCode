import re

#Calculate Multiples
def findTotal(string):
    total = 0
    for pair in re.findall(r"mul\(\d?\d?\d,\d?\d?\d\)", string):
        nums = pair.rstrip(")").lstrip("mul(").split(",")
        total += int(nums[0])*int(nums[1])
    return total

#Read File
with open("input.txt", "r") as f:
    input = f.read().replace("\n", "")

#Run and Output
print(f"Part One Answer: {findTotal(input)}")
print(f"Part Two Answer: {findTotal(re.sub(r"don't\(\)(.*?do\(\)|.*$)", "", input))}")
