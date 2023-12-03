with open("day_1_input.txt") as f:
    data = f.readlines()
result = 0
for line in data:
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    first = int(digits[0])
    last = int(digits[len(digits)-1])
    value = (first*10)+(last)
    result += value
result