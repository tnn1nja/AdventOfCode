file = open("input.txt", "r")
games = file.readlines()
file.close()

part1 = 0
part2 = 0

for gameNumber in range(len(games)):

    possible = True

    minRed = 0
    minGreen = 0
    minBlue = 0

    game = games[gameNumber].replace("\n", "").split(": ",1)[-1]
    rounds = []
    temp = game.split("; ")
    for item in temp:
        rounds.append(item.split(", "))
    
    for reveal in rounds:
        for cubes in reveal:
            number, color = cubes.split(" ")
            number = int(number)

            if (color == "red" and number > 12) or\
                (color == "green" and number > 13) or\
                (color == "blue" and number > 14):
                possible = False

            if color == "red" and number > minRed:
                minRed = number
            if color == "green" and number > minGreen:
                minGreen = number
            if color == "blue" and number > minBlue:
                minBlue = number

    if possible:
        part1 += gameNumber+1

    part2 += minRed*minBlue*minGreen

print(f"Part 1 Total = {part1}")
print(f"Part 2 Total = {part2}")