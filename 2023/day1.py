file = open("input.txt")
array = file.readlines()
file.close()

partOneAns = 0
partTwoAns = 0

def findNum(string):
    num = ""
    for char in string:
        if char.isdigit():
            num+=char
            break
    for char in reversed(string):
        if char.isdigit():
            num+=char
            break
    return int(num)

for string in array:

    partOneAns += findNum(string)
    
    string = string.replace("one", "o1e")
    string = string.replace("two", "t2o")
    string = string.replace("three", "t3e")
    string = string.replace("four", "f4r")
    string = string.replace("five", "f5e")
    string = string.replace("six", "s6x")
    string = string.replace("seven", "s7n")
    string = string.replace("eight", "e8t")
    string = string.replace("nine", "n9e")
    
    partTwoAns += findNum(string)

print(f"Part 1 Answer: {partOneAns}")
print(f"Part 2 Answer: {partTwoAns}")
