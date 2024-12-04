# A / X = ROCK
# B / Y = PAPER
# C / Z = SCISSORS

winners = {"A": "Y",
           "B": "Z",
           "C": "X"}

def getScoreFromInput(input):
    opponent, player = input
    score = ord(player)-87
    if winners.get(opponent) == player:
        return score + 6
    elif ord(player)-23 == ord(opponent):
        return score + 3
    else:
        return score

def getScoreFromOutcome(input):
    opponent, needed = input
    if needed == "Z":
        return getScoreFromInput([opponent, winners.get(opponent)])
    elif needed == "Y":
        return getScoreFromInput([opponent, chr(ord(opponent)+23)])
    else:
        player = ["X", "Y", "Z"]
        player.remove(chr(ord(opponent)+23))
        player.remove(winners.get(opponent))
        return getScoreFromInput([opponent, player[0]])

partOneAns = 0
partTwoAns = 0
with open("input.txt", "r") as f:
    for line in f:
        inputs = line.rstrip("\n").split(" ")
        partOneAns += getScoreFromInput(inputs)
        partTwoAns += getScoreFromOutcome(inputs)

print(f"Part One Answer: {partOneAns}")
print(f"Part Two Answer: {partTwoAns}")