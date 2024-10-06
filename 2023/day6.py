import re

#Read in File
f = open("input.txt", "r")
lines = f.readlines()
f.close()

#Extract Data for Part 1
times = re.sub(" +", " ", lines[0].split(":", 1)[1]).strip().split(" ")
distances = re.sub(" +", " ", lines[1].split(":", 1)[1]).strip().split(" ")
races = []
for i in range(len(times)):
    races.append([int(times[i]), int(distances[i])])

#Format Data for Part 2
megaRace = []
t = ""
d = ""
for values in races:
    t += str(values[0])
    d += str(values[1])
megaRace = [int(t), int(d)]

#Calculate Options
def calcOptions(race):
    options = 0
    for s in range(1, race[0]):
        if s*(race[0]-s) > race[1]:
            options += 1
    return options
            
#Calculate Part 1
partOneAns = 1
for race in races:
    partOneAns *= calcOptions(race)
    
#Calculate Part 2
partTwoAns = calcOptions(megaRace)
    
#Output
print(f"Part 1 Answer: {partOneAns}")
print(f"Part 2 Answer: {partTwoAns}")