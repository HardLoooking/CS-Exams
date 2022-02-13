try:
    in_file1= open("products.txt", "r")
    dict = {}
    for line in in_file1:
        line = line.strip()
        line = line.split()
        product = line[0]
        dealer = line[1]
        dict[product] = dealer

    in_file2 = open("purchases.txt", "r")
    purcharses = []    #Purchases
    for line in in_file2:
        line = line.strip()
        line = line.split()
        purcharses.append(line)


    fake = False
    first = True
    for i in range(len(purcharses)):
        fake_sup = []
        if purcharses[i][0] in dict:
            if purcharses[i][1] != dict[purcharses[i][0]]:
                fake_d = purcharses[i][1]
                fake_sup.append(fake_d)
                fake = True
                if fake:
                    if first:
                        print(f'Suspicious transactions list\n')
                        first = False
                        print(f'Product code: {purcharses[i][0]}\n'
                              f'Official dealer: {dict[purcharses[i][0]]}')
                        print(f'Dealer list: {dict[purcharses[i][0]]}', end=" ")
                        for i in range(len(fake_sup)):
                            print(fake_sup[i])
                        print()
                    else:
                        print(f'Product code: {purcharses[i][0]}\n'
                              f'Official dealer: {dict[purcharses[i][0]]}')
                        print(f'Dealer list: {dict[purcharses[i][0]]}',end=" ")
                        for i in range(len(fake_sup)):
                            print(fake_sup[i])
                        print()


    in_file1.close()
    in_file2.close()

except FileNotFoundError as Err:
    print(Err)