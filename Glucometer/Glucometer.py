"""
- Extract data
-Separate data (#patient, time and level of glucosa
- OPERATION
    who had at least one exceedance >200
    print first who has more exceedance

"""

in_file = open("glucometer.txt", "r")
patients = []
for element in in_file:
    line = element.strip()
    line = line.split(" ")
    patient = {}
    patient["Code"]=line[0]
    patient["Time"]=line[1]
    patient["Glucosa"]=float(line[2])
    patients.append(patient)

exc_pat = [] #List of exeedances that it got more than 200 glucosa
for i in patients:
    if i["Glucosa"] >= 200:
        exc_u = i
        exc_pat.append(exc_u)

empty_l1=[] #List of people who (no repeatable) got more than 200 glucosa
for i in range(len(exc_pat)):
    if not exc_pat[i]["Code"] in empty_l1:
        empty_l1.append(exc_pat[i]["Code"])


empty_l2 =[] #Sorting buy number of exeedances of each person, from the hightest to the lowest
for i in empty_l1:
    count = 0
    for y in exc_pat:
        if i == y["Code"]:
            count += 1
            a = [i, count]
    empty_l2.append(a)

empty_l2.sort(key=lambda x: x[1], reverse=True)


for y in range(0,len(empty_l2)):
    for i in range(0,len(exc_pat)):
        if empty_l2[y][0] == exc_pat[i]["Code"]:
            print(f'{exc_pat[i]["Code"]} {exc_pat[i]["Time"]} {exc_pat[i]["Glucosa"]}')
    print()


in_file.close()