from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

class Tree:
    def __init__(self, height, i, j) -> None:
        self.height = height
        self.i = i
        self.j = j
        self.score = 1

    def difference(self, other) -> int:
        return abs(self.i - other.i + self.j - other.j)

    def update(self, stack, counter):
        while stack and self.height > stack[-1].height:
            stack.pop()
        if not stack:
            #print(f"I am looking at an edge ({counter} trees)")
            self.score *= counter
        else:
            #print(f"I can see {tree.difference(stack[-1])} trees")
            self.score *= tree.difference(stack[-1])
        stack.append(self)

        #print(stack)

    def __repr__(self) -> str:
        return f"Tree at {self.i}-{self.j} with height {self.height}"

forest = [[Tree(int(file[i][j]), i, j) for j in range(len(file[i]))] for i in range(len(file))]

# horizontal
for i in range(len(file)):
    # left to right
    stack = []
    counter = 0
    #print("\n\nleft to right:")
    for j in range(len(file[i])):
        tree = forest[i][j]
        tree.update(stack, counter)
        counter += 1
    # right to left
    stack = []
    counter = 0
    #print("\n\nright to left:")
    for j in range(len(file[i])-1, -1, -1):
        tree = forest[i][j]
        tree.update(stack, counter)
        counter += 1
# vertical
for j in range(len(file[0])):
    # top to bottom
    stack = []
    counter = 0
    #print("\n\ntop to bottom:")
    for i in range(len(file)):
        tree = forest[i][j]
        tree.update(stack, counter)
        counter += 1
    # bottom to top
    stack = []
    counter = 0
    #print("\n\nbottom to top:")
    for i in range(len(file)-1, -1, -1):
        tree = forest[i][j]
        tree.update(stack, counter)
        counter += 1

best = 0
for line in forest:
    for tree in line:
        best = max(best, tree.score)
print(best)