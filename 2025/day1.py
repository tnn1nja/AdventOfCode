part_one = 0
part_two = 0

value = 50
was_zero = False
with open("input.txt", "r") as f:
    for line in f:
        operand = int(line[1:])
        if operand >= 100:
            part_two += operand // 100
            operand %= 100
            if operand == 0:
                part_one += 1
                continue
            
        if line[:1] =="R":
            value += operand
        else:
            value -= operand

        if not was_zero and (value < 0 or value > 100):
            part_two += 1
        value %=100 
        
        if value == 0:
            was_zero = True
            part_one += 1
            part_two += 1
        else:
            was_zero = False

print(f"Part One Answer: {part_one}")
print(f"Part Two Answer: {part_two}") 