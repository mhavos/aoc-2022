inf = float("inf")
IS_TEST = "test" if False else ""
file = open(IS_TEST+"input.txt", "r").read().strip("\n")#.split("\n")


for i in range(len(file)-3):
    if len(set(file[i:i+4])) == 4:
        break
print(i+4)