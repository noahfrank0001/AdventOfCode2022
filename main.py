txt = open("input.txt", "r")
input = txt.read()

elves = {}
addition = []
string = ""

splitStr = input.split("\n")

count = 0

for i in splitStr:
    if i.strip():
        addition.append(i)
    else:
        count += 1
        num = str(count)
        name = "Elf " + num
        elves[name] = addition
        addition = []

# If you uncomment this line, a dictionary with each elf and their calories will be returned.
# Note that the calories are currently in string form. This is because I didn't feel like going back and modifying it, lol
# print(elves)

maxNum = 0
maxElf = ""
for x, y in elves.items():
    for i in range(0, len(y)):
        y[i] = int(y[i])
    if sum(y) > maxNum:
        maxElf = x
        maxNum = sum(y)

print(maxElf, ":", str(maxNum))

