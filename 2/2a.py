inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip().split("\n")

convert = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

score = 0
for line in file:
    them, you = line.split()
    score += convert[you] + 3 + 3*((convert[you] - convert[them] + 1) % 3 - 1)
print(score)