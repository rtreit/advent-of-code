import re
with open("./input.txt") as f:
    data = f.read()
pattern = "mul\(.[0-9]*\,[0-9]*\)"
results = []
a = []
b = []
matches = re.findall(pattern, data)
for match in matches:
    x = match.split("(")[1].split(",")
    a.append(int(x[0]))
    b.append(int(x[1].replace(")", "")))
y = zip(a,b)
for i,j in y:
    results.append(i*j)
result_part_1 = sum(results)        
print(f"Part 1: {result_part_1}")

