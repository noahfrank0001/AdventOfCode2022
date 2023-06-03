txt = open("input.txt", "r")
input = txt.read()

elves = {}
addition = []
string = ""

splitStr = input.split("\n")

count = 0

for i in splitStr:
    if i.strip():
        addition.append(int(i))
    else:
        count += 1
        num = str(count)
        name = "Elf " + num
        elves[name] = addition
        addition = []

maxNum = 0
maxElf = ""
for x, y in elves.items():
    if sum(y) > maxNum:
        maxElf = x
        maxNum = sum(y)

elvesSorted = sorted(elves.items(), key=lambda z: sum(z[1]))

total = 0
for e in list(elvesSorted)[-3:]:
    total += sum(e[1])

print(total)

# Output: 206289