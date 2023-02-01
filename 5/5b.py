inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

stacks = {}
names = {}
s = file.index("")
first = True
for i in range(s-1, -1, -1):
    line = file[i]
    if first:
        first = False
        for j in range(len(line)):
            if line[j] != " ":
                names[line[j]] = j
                stacks[j] = []
    else:
        for j in stacks:
            if line[j] != " ":
                stacks[j].append(line[j])
for i in range(s+1, len(file)):
    line = file[i]
    howmany, where = line.strip("move ").split(" from ")
    fro, to = where.split(" to ")
    stacks[names[to]].extend(stacks[names[fro]][-int(howmany):])
    stacks[names[fro]] = stacks[names[fro]][:-int(howmany)]
vs = list(stacks.items())
vs.sort()
for v in vs:
    print(v[1].pop(), end="")
print()