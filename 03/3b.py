inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip().split("\n")

c = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
for i in range(0, len(file), 3):
    lines = [set(line) for line in file[i:i+3]]
    total += c.find((lines[0] & lines[1] & lines[2]).pop())
print(total)
