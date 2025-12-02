def has_equal_segments(string, length):
    segments = set()
    substring = ""
    for char in string:
        substring += char
        if len(substring) == length:
            segments.add(substring)
            substring = ""
    return len(segments) == 1

def is_invalid_part_one(id):
    str_id = str(id)
    if len(str_id)%2 == 0:
        return has_equal_segments(str_id, len(str_id)//2)

def is_invalid_part_two(id):
    str_id = str(id)
    for length in range(1, len(str_id)//2+1):
        if len(str_id) % length == 0:
            if has_equal_segments(str_id, length):
                return True
    return False
            
with open("input.txt", "r") as f:
    ranges = [[int(x) for x in y.split("-")] for y in f.readline().split(",")]

part_one = 0
part_two = 0
for r in ranges:
    for id in range(r[0], r[1]+1):
        if is_invalid_part_one(id):
                part_one += id
        if is_invalid_part_two(id):
                part_two += id


print(f"Part One Answer: {part_one}")
print(f"Part Two Answer: {part_two}")