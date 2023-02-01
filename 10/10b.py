from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

vals = []
X = 1
for line in file:
    vals.append(X)
    if line != "noop":
        vals.append(X)
        X += int(line.split()[1])

result = ["#" if i%40-1 <= vals[i] <= i%40+1 else "." for i in range(len(vals))]
result = "\n".join(["".join(result[40*i:40*(i+1)]) for i in range(6)])
print(result)