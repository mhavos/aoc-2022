inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip().split("\n")

best = -inf
current = 0
for line in file:
    if line == "\n":
        best = max(best, current)
        current = 0
    else:
        current += int(line)
print(best)