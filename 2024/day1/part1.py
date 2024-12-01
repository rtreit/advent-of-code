import pandas as pd
with open ("day1/input.txt", "r") as file:
    data = file.read().split("\n")
a = []
b = []
x = [d.split("   ") for d in data]
for i in x:
    a.append(int(i[0]))
    b.append(int(i[1]))
a.sort()
b.sort()
df = pd.DataFrame(columns=["a", "b", "c"])
df.a = a
df.b = b
df.c = abs(df.a - df.b)
result = df.c.sum()
print(result)