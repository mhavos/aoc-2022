from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

class File:
    def __init__(self, size) -> None:
        self.size = size

    def evaluate(self) -> tuple[int, int]:
        return (0, self.size)

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

    def evaluate(self) -> tuple[int, int]:
        total, size = 0, 0
        for name in self.children:
            child = self.children[name]
            t, s = child.evaluate()
            total += t
            size += s
        if size <= 100_000:
            total += size
        return (total, size)

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

print(root.evaluate()[0])