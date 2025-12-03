def get_max_value(values, first_index, last_index):
    max_value = 0
    max_value_index = 0
    for i in range(first_index, last_index):
        current_value = int(values[i])
        if current_value > max_value:
            max_value = current_value
            max_value_index = i
            if max_value == 9:
                break
    return max_value, max_value_index

part_one = 0
part_two = 0
with open("2025/input.txt", "r") as f:
    for bank in f:
        bank = bank.rstrip("\n")
        first_value, first_index = get_max_value(bank, 0, len(bank)-1)  #0
        second_value = get_max_value(bank, first_index+1, len(bank))[0] #1
        part_one += int(f"{first_value}{second_value}")

        long_joltage = ""
        first_index = -1
        for i in range(12):
            value, first_index = get_max_value(bank, first_index+1, len(bank)-(11-i))
            long_joltage += str(value)
        part_two += int(long_joltage)


print(f"Part One Answer: {part_one}")
print(f"Part Two Answer: {part_two}")