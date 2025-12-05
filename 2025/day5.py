with open("input.txt", "r") as f:
    lines = f.readlines()

ranges = []
ids = []
is_ranges = True
for line in lines:
    line = line.rstrip("\n")
    if line == "":
        is_ranges = False
        continue
    if is_ranges:
        ranges.append([int(x) for x in line.split("-")])
    else:
        ids.append(int(line))

ranges.sort(key=lambda x: x[0])
i = 0
while i < len(ranges)-1:
    if ranges[i][0] <= ranges[i+1][0] <= ranges[i][1]:
        ranges[i][1] = ranges[i+1][1]
        ranges.pop(i+1)
    else:
        i+=1

part_one = 0
for id in ids:
    for range in ranges:
        if range[0] <= id <= range[1]:
            part_one += 1
            break

part_two = 0
for r in ranges:
    part_two += r[1]-r[0]+1

print(f"Part One Answer: {part_one}") #690
print(f"Part Two Answer: {part_two}")