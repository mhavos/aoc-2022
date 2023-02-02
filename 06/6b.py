inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n")#.split("\n")

n = 14

for i in range(len(file)-n+1):
    if len(set(file[i:i+n])) == n:
        break
print(i+n)