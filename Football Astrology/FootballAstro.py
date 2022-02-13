try:
    file_1 = open("sportivi.csv","r")
    dict={}
    names = [] #List of names, non repeatable
    for line in file_1:
        line = line.strip()
        line = line.split(",")
        name = line[0]
        goals = int(line[1])
        country= line[2]
        birthday = line[3].split("/")
        date = int(birthday[1]+birthday[0])
        dict[name] = [goals, date]
        names.append(name)


    file_2 = open("zodiaco.csv", "r")

    signes = []
    for line in file_2:
        line = line.strip()
        line = line.split(",")
        pre_list = []
        n_signe = line[0]
        i_pre = line[1].split("/")
        i_date = int(i_pre[1]+i_pre[0])
        f_pre = line[2].split("/")
        f_date = int(f_pre[1] + f_pre[0])
        count = 0 #Accumulative of goals of each sign
        proportion = 0 #Proportion of the asterisks
        pre_list.append(n_signe)
        pre_list.append(i_date)
        pre_list.append(f_date)
        pre_list.append(count)
        pre_list.append(proportion)
        signes.append(pre_list)

    #Operation
    #Players: Abe Lenstra': [710, 1127],            #Signes ['Aries', 321, 420, 0]
    for i in range(len(dict)):
        for y in range(len(signes)):
            if dict[names[i]][1] >= signes[y][1] and dict[names[i]][1] <= signes[y][2]:
                signes[y][3] += dict[names[i]][0]

    signes.sort(key=lambda x: x[3], reverse=True)

    max_1 = 0
    min_1 = 0
    for element in signes:
        if element[3]> max_1:
            max_1 = element[3]
        if element[3] < min_1:
            min_1 = element[3]
        element[4] = round((element[3]*50 / max_1))
        print(f'{element[0]:<15s} ({element[3]}) {element[4]*"*"}')

    file_1.close()
    file_2.close()

except FileNotFoundError as Err:
    print("File not found")
finally:
    print("Program executed")