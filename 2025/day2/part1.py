with open("input.txt") as f:
    input: list = f.readline().split(",")


def split_even_number(number: int) -> tuple:
    number: str = str(number)
    digit_size: int = int(len(number) / 2)
    a = (number[:digit_size])
    b = (number[digit_size:])
    return (a,b)

def find_duplicates(input) -> list:
    invalid_values = []
    input = input.split("-")
    candidates: list = range(int(input[0]), int(input[1]) + 1)
    tracker: dict = {}
    for i in candidates:
        id_length: int = len(str(i))
        tracker.setdefault(i, {"length": id_length, "count": 0})
        tracker[i]["count"] = tracker[i]["count"] + 1
    uneven = []
    for k, v in tracker.items():
        if v["length"] % 2 != 0:
            uneven.append(k)
    [tracker.pop(k) for k in uneven]
    for k in tracker.keys():
        split_result = split_even_number(k)
        if split_result[0] == split_result[1]:
            print(f"Found invalid value: {k}")
            invalid_values.append(k)
    return invalid_values

results = []
tracker = find_duplicates(input[0])
for i in enumerate(input):
    results = results + find_duplicates(i[1])
    
print(results)
print(f"Sum of invalid IDs: {sum(results)}")