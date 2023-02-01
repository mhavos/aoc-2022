from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n\n")

class Monkey:
    def __init__(self, i, items, operation, test, if_true, if_false):
        self.i = i
        self.items = items
        op = (lambda c, d: c+d) if operation[1] == "+" else (lambda c, d: c*d)
        self.operation = lambda a: op(*[a if operation[i] == "old" else int(operation[i]) for i in (0, 2)])
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

        self.inspected = 0

    def throw(self, item):
        self.inspected += 1

        item = self.operation(item)
        item %= modconst
        if not item%self.test:
            monkeys[self.if_true].items.append(item)
        else:
            monkeys[self.if_false].items.append(item)
    
    def clear(self):
        for item in self.items:
            self.throw(item)
        
        self.items = []

    def __repr__(self) -> str:
        return f"monkey {self.i}"

monkeys = []

for group in file:
    group = group.split("\n")
    i = int(group[0].strip().split("Monkey ")[1].strip(":"))
    items = list(map(int, group[1].strip().split("Starting items: ")[1].split(", ")))
    operation = group[2].strip().split("Operation: new = ")[1].split()
    test = int(group[3].strip().split("Test: divisible by ")[1])
    if_true = int(group[4].strip().split("If true: throw to monkey ")[1])
    if_false = int(group[5].strip().split("If false: throw to monkey ")[1])
    monkeys.append(Monkey(i, items, operation, test, if_true, if_false))

def round():
    for monkey in monkeys:
        monkey.clear()

modconst = 1
for monkey in monkeys: modconst *= monkey.test

for _ in range(10000):
    round()

import heapq
q = []
for monkey in monkeys:
    heapq.heappush(q, -monkey.inspected)
print(heapq.heappop(q)*heapq.heappop(q))