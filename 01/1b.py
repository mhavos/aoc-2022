inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip().split("\n")

import heapq

heap = []
current = 0
for line in file:
    if line == "\n":
        heapq.heappush(heap, -current)
        current = 0
    else:
        current += int(line)
print(-sum([heapq.heappop(heap) for i in range(3)]))