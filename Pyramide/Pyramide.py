try:
    in_file = open("mp.txt", "r")

    maptotal = []
    for line in in_file:
        line = line.strip()
        line = line.split(" ")
        colum = []
        for number in line:
            a = int(number)
            colum.append(a)
        maptotal.append(colum)


    maximuns = []
    max_1 = 0
    for i in range(len(maptotal)):  #rows

        for y in range(len(maptotal[0])):  #columns

            adiacente = [] #Values at the surroundings of the central
            for r in [i - 1, i, i + 1]:
                if 0 <= r < len(maptotal):
                    for q in [y - 1, y, y + 1]:
                        if 0 <= q < len(maptotal[0]):
                            if (r != i) or (q != y):
                                adiacente.append(maptotal[r][q])

            if maptotal[i][y] > max(adiacente):
                pre_list = []
                num = maptotal[i][y]
                row = i
                colum = y
                pre_list.append(num)
                pre_list.append(row)
                pre_list.append(colum)
                maximuns.append(pre_list)

    sum_avg=0
    for i in maximuns:
        print(i[0],i[1],i[2])
        sum_avg += i[0]
    print()
    print(f'Average height: {sum_avg/len(maximuns)} m.')

    in_file.close()

except FileNotFoundError:
    print("File not found")
finally:
    print("Program was tried")