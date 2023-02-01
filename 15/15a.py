from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n")

row = 2000000
filled = [(inf, inf)]
beacons = set()

for line in file:
    coords = list(map(lambda s: list(map(int, s.split(", y="))), line.strip("Sensor at x=").split(": closest beacon is at x=")))
    dist = abs(coords[0][0] - coords[1][0]) + abs(coords[0][1] - coords[1][1])
    
    if coords[1][1] == row:
        beacons.add(tuple(coords[1]))

    if abs(coords[0][1] - row) > dist:
        continue

    dif = dist - abs(coords[0][1] - row)
    start = coords[0][0] - dif
    end = coords[0][0] + dif + 1

    newfilled = []
    phase = -1
    for segment in filled:
        if phase == -1:
            if segment[1] < start:
                newfilled.append(segment)
            elif segment[0] > end:
                phase = 1
                newfilled.append((start, end))
                newfilled.append(segment)
            elif segment[1] > end:
                phase = 1
                newfilled.append((min(start, segment[0]), segment[1]))
            else:
                phase = 0
                current = min(start, segment[0])
        elif phase == 0:
            if segment[0] > end:
                phase = 1
                newfilled.append((current, end))
                newfilled.append(segment)
            elif segment[1] >= end:
                phase = 1
                newfilled.append((current, segment[1]))
        else:
            newfilled.append(segment)
    filled = newfilled
    print(filled)

total = 0
for segment in filled[:-1]:
    total += segment[1] - segment[0]
print(total - len(beacons))
