from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

vals = [None]
X = 1
for line in file:
    vals.append(X)
    if line != "noop":
        vals.append(X)
        X += int(line.split()[1])

total = 0
for i in range(20, len(vals), 40):
    total += i*vals[i]

print(total)