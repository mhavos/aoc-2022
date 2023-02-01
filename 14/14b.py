from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

SOURCE = -1
AIR = 0
ROCK = 1
SAND = 2

trans = {SOURCE:"+", AIR: ".", ROCK: "#", SAND: "o"}
def draw(start, end):
    for y in range(maxy):
        for x in range(start, end+1):
            print(trans[grid.get((x, y), AIR)], end="")
        print()
    print("#"*(end-start+1))

maxy = -inf
minx, maxx = inf, -inf
source = (500, 0)
grid = {source: SOURCE}
for line in file:
    coords = list(map(lambda c: tuple(map(int, c.split(","))), line.split(" -> ")))
    current = coords[0]
    maxy = max(maxy, current[1])
    grid[current] = ROCK
    for next in coords[1:]:
        maxy = max(maxy, next[1])
        minx = min(minx, next[0])
        maxx = max(maxx, next[0])
        for x in range(min(current[0], next[0]), max(current[0], next[0]) + 1):
            for y in range(min(current[1], next[1]), max(current[1], next[1]) + 1):
                grid[x, y] = ROCK
        current = next
maxy += 2

resting = 0
previous = []
current = source
while True:
    for offset in (0, -1, 1):
        next = (current[0] + offset, current[1] + 1)
        if next[1] < maxy and grid.get(next, AIR) == AIR:
            previous.append(current)
            current = next
            break
    else:
        grid[current] = SAND
        resting += 1
        if previous:
            current = previous.pop()
        else:
            break
draw(minx, maxx)
print(resting)