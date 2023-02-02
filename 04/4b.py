inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip().split("\n")

total = 0
for line in file:
    (a1, a2), (b1, b2) = tuple(map(lambda y: tuple(map(int, y.split("-"))), line.split(",")))
    total += ((a1 <= b1) and (a2 >= b2)) or ((a1 >= b1) and (a2 <= b2)) or (a1 <= b1 <= a2) or (a1 <= b2 <= a2)
print(total)
