f = open("input.txt", "r")
lines = f.readlines()
f.close()

#Number Array Formatter
def numArrayFormat(string):
    string = string.strip(" ").replace("  ", " ")
    output = string.split(" ")
    for i in range(len(output)):
        output[i] = int(output[i])
    return output

#Format Array
cards = []
for i in range(len(lines)):
    lines[i] = lines[i].split(": ", 1)[1].replace("\n", "")
    winningStr, rolledStr = lines[i].split(" | ")
    winning = numArrayFormat(winningStr)
    rolled = numArrayFormat(rolledStr)
    cards.append([winning, rolled])

#Find Matching Cards
calcCards = []
for card in cards:
    matches = 0
    for num in card[1]:
        if num in card[0]:
            matches += 1
    calcCards.append([card[0], card[1], matches, 1])

#Find Number of Cards
for i in range(len(calcCards)):
    matches = calcCards[i][2]
    for x in range(calcCards[i][3]):
        for j in range(matches):
            calcCards[i+j+1][3] += 1


#Find Part 1 Answer
partOneTotal = 0
for card in calcCards:
    score = 2**(card[2]-1)
    if score >= 1:
        partOneTotal += score

#Find Part 2 Answer
partTwoTotal = 0
for card in calcCards:
    partTwoTotal += card[3]

print(f"Part 1 Total: {partOneTotal}")
print(f"Part 2 Total: {partTwoTotal}")
