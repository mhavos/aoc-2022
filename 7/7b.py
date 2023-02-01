from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

class File:
    def __init__(self, size) -> None:
        self.size = size

    def evaluate(self, needed=0) -> tuple[int, int]:
        if needed <= self.size:
            return (self.size, self.size)
        else:
            return (inf, self.size)

class Dir:
    def __init__(self, parent) -> None:
        self.children = {}
        self.parent = parent

    def ls(self, size, name) -> None:
        if name in self.children:
            pass
        elif size == "dir":
            self.children[name] = Dir(self)
        else:
            self.children[name] = File(int(size))

    def cd(self, name) -> Dir:
        return self.children[name]

    def evaluate(self, needed=0) -> tuple[int, int]:
        best, size = inf, 0
        for name in self.children:
            child = self.children[name]
            b, s = child.evaluate(needed)
            best = min(best, b)
            size += s
        if needed <= size:
            best = min(best, size)
        return (best, size)

root = Dir(None)
for line in file:
    if line[0] == "$":
        if line[0:4] == "$ ls":
            continue
        *_, name = line.split()
        if name == "/":
            current = root
        elif name == "..":
            current = current.parent
        else:
            current = current.cd(name)
    else:
        size, name = line.split()
        current.ls(size, name)

print(root.evaluate(needed=root.evaluate()[1]-40_000_000)[0])