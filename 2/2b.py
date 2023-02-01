inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip().split("\n")

convert = {"A": 0, "B": 1, "C": 2, "X": -1, "Y": 0, "Z": 1}

score = 0
for line in file:
    them, you = line.split()
    score += 1 + (convert[them] + convert[you])%3 + (convert[you] + 1)*3
print(score)