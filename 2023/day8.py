#Read in File
f = open("input.txt", "r")
lines = f.readlines()
f.close()

#Extract Data
path = lines[0].rstrip("\n")
maps = {}
mapStrings = lines[2:]
for string in mapStrings:
    data = string.rstrip("\n)").replace(" = (", " ").replace(", ", " ").split(" ")
    maps[data[0]] = [data[1], data[2]]

#Get Next Node
def getNextNode(node, moves):
    if path[moves % len(path)] == "L":
        return maps[node][0]
    else:
        return maps[node][1]

#Find Part 1
partOneNode = "AAA"
partOneAns = 0
while True:
    if partOneNode == "ZZZ":
        break
    partOneNode = getNextNode(partOneNode, partOneAns)
    partOneAns += 1

print(f"Part 1 Answer: {partOneAns}")

#Find Part 2
partTwoNodes = []
for key in maps.keys():
    if key[-1] == "A":
        partTwoNodes.append(key)
print(f"Part Two Nodes: {partTwoNodes}")

partTwoAns = 0
while True:
    finishingNodes = 0
    for i in range(len(partTwoNodes)):
        if partTwoNodes[i][-1] == "Z":
            finishingNodes += 1
        partTwoNodes[i] = getNextNode(partTwoNodes[i], partTwoAns)
    if finishingNodes == len(partTwoNodes):
        break
    partTwoAns += 1
    if partTwoAns % 1000000 == 0:
        print(f"Part 2 > {partTwoAns}")
    
print(f"Part 2 Answer: {partTwoAns}")