def generate_line_tuple(line) -> tuple:
    try:
        line_tuple: tuple = (line[0], int(line[1:]))
        return line_tuple
    except Exception as e:
        print(f"Hit an exception: {e}")
        return {}

def turn_dial(dial: list, current_index: int, step:int, direction: str, zero_count: int) -> int:
    min_value = min(dial)
    max_value = max(dial)
    for _ in range(step):
        if direction == "L":
            if current_index == min_value:
                current_index = max_value               
            else:
                current_index = current_index - 1
        if direction == "R":
            if current_index == max_value:
                current_index = min_value                
            else:
                current_index = current_index + 1
        if current_index == 0:
            zero_count += 1
    return current_index, zero_count

dial = [x for x in range(100)]
current_index = 50
with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

line_tuples = [generate_line_tuple(line) for line in lines]
zero_count = 0
for t in line_tuples:
    current_index, zero_count = turn_dial(dial, current_index, t[1], t[0], zero_count)
print(zero_count)
