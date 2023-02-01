from __future__ import annotations

inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n").split("\n\n")

class Packet:
    def __init__(self, text) -> None:
        self.data = []
        stack = [[0]]
        for i in range(len(text)):
            char = text[i]
            if char == "[":
                new = [] if text[i+1] == "]" else [0]
                stack[-1][-1] = new
                stack.append(new)
            elif char == "]":
                stack.pop()
            elif char == ",":
                stack[-1].append(0)
            else:
                stack[-1][-1] = stack[-1][-1]*10 + int(char)
        self.data = stack[0][0]

    @classmethod
    def le(self, left, right):
        if type(left) is type(right) is int:
            if left < right:
                return True
            elif left == right:
                return None
            else:
                return False
        elif type(left) is int:
            left = [left]
        elif type(right) is int:
            right = [right]

        for i in range(min(len(left), len(right))):
            comp = Packet.le(left[i], right[i])
            if comp in (True, False):
                return comp

        if len(left) < len(right):
            return True
        elif len(left) == len(right):
            return None
        else:
            return False

    def __lt__(self, other):
        return Packet.le(self.data, other.data) in (True, None)

    def __repr__(self):
        return repr(self.data)

dividers = [Packet("[[2]]"), Packet("[[6]]")]
packets = dividers.copy()

for i in range(len(file)):
    lines = file[i].split("\n")
    packets.append(Packet(lines[0]))
    packets.append(Packet(lines[1]))
packets.sort()

print((packets.index(dividers[0]) + 1) * (packets.index(dividers[1]) + 1))