from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

class Tree:
    def __init__(self, height, i, j) -> None:
        self.height = height
        self.i = i
        self.j = j
        self.visible = False

forest = [[Tree(int(file[i][j]), i, j) for j in range(len(file[i]))] for i in range(len(file))]

# horizontal
for i in range(len(file)):
    # left to right
    tallest = -inf
    for j in range(len(file[i])):
        tree = forest[i][j]
        if tree.height > tallest:
            tree.visible = True
            tallest = tree.height
    # right to left
    tallest = -inf
    for j in range(len(file[i])-1, -1, -1):
        tree = forest[i][j]
        if tree.height > tallest:
            tree.visible = True
            tallest = tree.height
# vertical
for j in range(len(file[0])):
    # top to bottom
    tallest = -inf
    for i in range(len(file)):
        tree = forest[i][j]
        if tree.height > tallest:
            tree.visible = True
            tallest = tree.height
    # bottom to top
    tallest = -inf
    for i in range(len(file)-1, -1, -1):
        tree = forest[i][j]
        if tree.height > tallest:
            tree.visible = True
            tallest = tree.height

total = 0
for line in forest:
    for tree in line:
        total += tree.visible
print(total)