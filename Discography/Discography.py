try:
    in_file_1 = open("artist.txt", "r")

    artist = []
    for element in in_file_1:
        element = element.strip()
        element = element.split(";")
        artist.append(element)

    list_1 = []
    new_set = set()

    for i in range(len(artist)):
        a = open(artist[i][1], "r")
        b = [artist[i][0]] #Name of the band or artist
        dict = {}
        for element in a:
            element = element.strip()
            element = element.split(";")
            year = int(element[0])
            song = element[1]
            new_set.add(year)
            dict[year] = [song, b]
        list_1.append(dict)

        a.close()
    new_list = sorted(new_set)

    first = True
    for y in range(len(new_list)):
        for i in range(len(list_1)):
            if new_list[y] in list_1[i]:
                if first:
                    print(new_list[y])
                    print(f'{list_1[i][new_list[y]][0]:<30s}                 {list_1[i][new_list[y]][1][0]}')
                    first = False
                else:
                    print(f'{list_1[i][new_list[y]][0]:<30s}                 {list_1[i][new_list[y]][1][0]}')
        first = True

    in_file_1.close()

except FileNotFoundError as err:
    print("File not found")



