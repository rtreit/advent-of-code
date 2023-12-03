import re
with open("input.txt") as f:
    data = f.readlines()
results = 0
for line in data:
    positions = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    digit_dict = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    for key in digit_dict:
        matches = [match.start() for match in re.finditer(key, line)]
        if matches != positions[digit_dict[key]]:
            positions[digit_dict[key]] = positions[digit_dict[key]] + matches       
    for char in line:
        if char.isdigit():
            matches = [match.start() for match in re.finditer(char, line)]
            if matches != positions[int(char)]:
                positions[int(char)] = positions[int(char)] + matches         
    updated = {}
    for k, v in positions.items():
        if len(v) > 0:
            updated[k] = list(set(v))
    result = []
    least = {}
    most = {}
    for k, v in updated.items():
        least[min(v)] = k
    for k, v in updated.items():
        most[max(v)] = k    
    updated
    least = least[min(least.keys())]
    most = most[max(most.keys())]    
    value = least*10+most
    results += value
print(results)