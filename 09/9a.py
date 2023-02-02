from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

visited = set()
headpos = (0, 0)
tailpos = (0, 0)
visited.add(tailpos)

def dist():
    return max(abs(headpos[0] - tailpos[0]), abs(headpos[1] - tailpos[1]))

def move(dir, n):
    global headpos, tailpos
    for _ in range(n):
        prevpos = headpos
        headpos = (headpos[0] + dir[0], headpos[1] + dir[1])
        if dist() > 1:
            tailpos = prevpos
            visited.add(tailpos)

dirs = {"R": (0, 1), "U": (1, 0), "L": (0, -1), "D": (-1, 0)}
for line in file:
    dir, n = line.split()
    move(dirs[dir], int(n))
print(len(visited))