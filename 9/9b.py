from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

def sign(n):
    return 1 if n > 0 else -1 if n < 0 else 0

class Rope:
    def __init__(self, n) -> None:
        self.pos = [0, 0]
        self.n = n

        if n == 0:
            self.visited = set()
            self.visited.add(tuple(self.pos))
            self.result = lambda: len(self.visited)
        else:
            self.next = Rope(n-1)
            self.result = self.next.result

    def update(self, headpos):
        if max(abs(headpos[0] - self.pos[0]), abs(headpos[1] - self.pos[1])) <= 1:
            return

        if headpos[0] == self.pos[0]:
            self.pos[1] += sign(headpos[1] - self.pos[1])

        elif headpos[1] == self.pos[1]:
            self.pos[0] += sign(headpos[0] - self.pos[0])

        else:
            self.pos[0] += sign(headpos[0] - self.pos[0])
            self.pos[1] += sign(headpos[1] - self.pos[1])

        if self.n == 0:
            self.visited.add(tuple(self.pos))
        else:
            self.next.update(self.pos)

    def move(self, dir, n):
        for _ in range(n):
            self.pos[0] += dir[0]
            self.pos[1] += dir[1]
            self.next.update(self.pos)
            #print(f"\t{self}")

    def __repr__(self) -> str:
        if self.n == 0:
            return f"{self.pos}"
        else:
            return f"{self.pos}-{self.next}"

dirs = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
rope = Rope(9)
for line in file:
    dir, n = line.split()
    #print(line)
    rope.move(dirs[dir], int(n))
print(rope.result())
