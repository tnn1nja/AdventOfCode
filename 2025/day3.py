def get_max_single_value(values, first_index, last_index):
    max_value = 0
    max_value_index = 0
    for i in range(first_index, last_index):
        current_value = int(values[i])
        if current_value > max_value:
            max_value = current_value
            max_value_index = i
            if max_value == 9:
                break
    return max_value, max_value_index+1

def get_max_joined_value(values, length):
    max_value = ""
    first_index = 0
    for i in range(length):
        last_index = len(values)-(length-1-i)
        value, first_index = get_max_single_value(bank, first_index, last_index)
        max_value += str(value)
    return int(max_value)

part_one = 0
part_two = 0
with open("2025/input.txt", "r") as f:
    for bank in f:
        bank = bank.rstrip("\n")
        part_one += get_max_joined_value(bank, 2)
        part_two += get_max_joined_value(bank, 12)

print(f"Part One Answer: {part_one}")
print(f"Part Two Answer: {part_two}")