totals = []
total = 0
with open("input.txt", "r") as f:
    for line in f:
        if line == "\n":
            totals.append(total)
            total = 0
        else:
            total += int(line.rstrip("\n"))
totals.sort(reverse=True)

print(f"Part One Answer: {totals[0]}")
print(f"Part Two Answer: {totals[0] + totals[1] + totals[2]}")