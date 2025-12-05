with open("test.txt", "r") as f:
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

def is_fresh(id):
    for range in ranges:
        if range[0] <= id <= range[1]:
            return True
    return False

part_one = 0
for id in ids:
    part_one += is_fresh(id)

part_two = 0
#sort by starting id - collapse based on starting id

print(f"Part One Answer: {part_one}")
print(f"Part Two Answer: {part_two}")