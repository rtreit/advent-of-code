import re

with open("./input.txt") as f:
    data = f.read()

# part 1
def add_muls(input: str):
    mul_pattern = r"mul\(.[0-9]*\,[0-9]*\)"
    results = []
    a = []
    b = []
    matches = re.findall(mul_pattern, input)
    for match in matches:
        x = match.split("(")[1].split(",")
        a.append(int(x[0]))
        b.append(int(x[1].replace(")", "")))
    y = zip(a,b)
    for i,j in y:
        results.append(i*j)
    return results

part_1 = sum(add_muls(data))
print(f"Part 1: {part_1}")

# part 2
enabled_muls = []
def find_the_muls(data):
    disabled_index = data.find("don't()")
    if disabled_index > -1:
        input = data[:disabled_index]
        muls = add_muls(input)
        for mul in muls:
            enabled_muls.append(mul)
        new_input = data[disabled_index+7:]
        enabled_index = new_input.find("do()")
        if enabled_index > -1:
            find_the_muls(new_input[enabled_index+4:])
find_the_muls(data)
part_2 = sum(enabled_muls)
print(f"Part 2: {part_2}")    