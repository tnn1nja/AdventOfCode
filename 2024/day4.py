#Read in File
with open("input.txt", "r") as f:
    lines = [x.rstrip("\n") for x in f.readlines()]

#Calculate Part One
def isValidXmasOrigin(i, y, j, x):
    return (i+(y*3) >= 0 and i+(y*3) < len(lines) and\
             j+(x*3) >= 0 and j+(x*3) < len(lines[0])) and\
            lines[i+y][j+x] == "M" and\
            lines[i+(y*2)][j+(x*2)] == "A" and\
            lines[i+(y*3)][j+(x*3)] == "S"

#Calculate Part Two
letters = ["M", "S"]
def isValidMasOrigin(i,j):
    return lines[i][j] == "A" and\
          (i >= 1 and i < len(lines)-1 and\
           j >= 1 and j < len(lines[0])-1) and\
           sorted([lines[i-1][j-1],lines[i+1][j+1]]) == letters and\
           sorted([lines[i-1][j+1],lines[i+1][j-1]]) == letters

#Iterate Through and Run
partOneAns = 0
partTwoAns = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "X":
            for y in range(-1,2):
                for x in range(-1,2):
                    if isValidXmasOrigin(i,y,j,x):
                        partOneAns += 1
        if isValidMasOrigin(i,j):
            partTwoAns += 1

#Output
print(f"Part One Answer: {partOneAns}")
print(f"Part Two Answer: {partTwoAns}")