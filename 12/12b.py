from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

first = None
last = None
def found(char, i, j):
    global first, last
    if char == "S":
        first = (i, j)
        return ord("a")
    elif char == "E":
        last = (i, j)
        return ord("z")
    else:
        return ord(char)

file = [[found(file[i][j], i, j) for j in range(len(file[i]))] for i in range(len(file))]

from collections import deque
q = deque()
q.append((last, 0))
visited = set()
best = inf

while q:
    current, i = q.popleft()
    if current in visited:
        continue
    visited.add(current)
    if file[current[0]][current[1]] == ord("a"):
        best = min(best, i)

    for dir in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        next = (current[0] + dir[0], current[1] + dir[1])
        if 0 <= next[0] < len(file) and 0 <= next[1] < len(file[next[0]]) and file[next[0]][next[1]] + 1 >= file[current[0]][current[1]]:
            q.append((next, i+1))

print(best)
