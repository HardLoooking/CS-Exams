in_file = open("bowling.txt")
names = []
score = []
strikes = []
none = []
for line in in_file:
    str = 0
    null = 0
    count = 0
    line = line.strip()
    element = line.split(";")
    name = element[1] + " " + element[0]
    names.append(name)
    for y in range(2,len(element)):
        count += int(element[y])
        if element[y] == "10":
            str += 1
        elif element[y] == "0":
            null += 1
    strikes.append(str)
    none.append(null)
    score.append(count)

new_names = names[:]
for z in range(0,len(new_names)):
    top = max(score)
    idx = score.index(top)
    print(new_names[idx], score[idx])
    score.pop(idx)
    names.pop(idx)


top_1 = max(strikes)
idxl = strikes.index(top_1)

print(f'{new_names[idxl]} has knocked down all the pins {strikes[idxl]} times')

low_1 = max(none)
idxl2 = none.index(low_1)
print(f"{new_names[idxl2]} has missed all the pins {none[idxl2]} time (s)")