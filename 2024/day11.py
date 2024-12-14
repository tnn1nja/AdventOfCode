#Find Next Stone Layout
def getNextStoneLayout(stones):
    newStones = []
    for stone in stones:
        if stone == 0:
            newStones.append(1)
        else:
            strStone = str(stone)
            lenStrStone = len(strStone)
            if len(strStone)%2 == 0:
                newStones.append(int(strStone[:lenStrStone//2]))
                newStones.append(int(strStone[lenStrStone//2:]))
            else:
                newStones.append(stone*2024)
    return newStones

#Read in file
with open("test.txt", "r") as f:
    stones = [int(num) for num in f.read().split(" ")]

#Part One
for i in range(25):
    stones = getNextStoneLayout(stones)
print(f"Part One Answer: {len(stones)}")

#Part Two
for i in range(50):
    print(f"Part Two Progress {i+25}/75")
    stones = getNextStoneLayout(stones)
print(f"Part Two Answer: {len(stones)}")