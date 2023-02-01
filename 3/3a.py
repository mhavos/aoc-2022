inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip().split("\n")

c = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
for line in file:
    total += c.find((set(line[:len(line)//2]) & set(line[len(line)//2:])).pop())
print(total)
