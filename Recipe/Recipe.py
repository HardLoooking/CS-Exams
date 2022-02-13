try:
    in_file1 = open("food.txt", "r")

    dict = {}
    for line in in_file1:
        line = line.strip()
        line = line.split(";")
        ingredient = line[0].strip()
        cost = float(line[1].strip())/1000 #Cost per KG
        calories = float(line[2].strip())/1000 #Calories per KG
        dict[ingredient]= [cost, calories]


    in_file2 = open("fusilli_alle_olive.txt", "r")

    read_recipe =[]
    line = False
    while line != "":
        line = in_file2.readline().strip()
        read_recipe.append(line)

    read_recipe.pop(0)
    read_recipe.pop(-1)


    recipe = []
    for line in read_recipe:
        line = line.split(";")
        info = []
        ing = line[0]
        cant = float(line[1].strip())
        info.append(ing)
        info.append(cant)
        recipe.append(info)


    #Operation
    first = True
    num = 0
    cost_rec = 0
    cant_cal = 0
    for i in range(len(recipe)):
        if first:
            print('Ingredients:')
            first = False
            print(f'{recipe[i][0]} - {recipe[i][1]*dict[recipe[i][0]][1]}')
            num = 1
            cost_rec += recipe[i][1]*dict[recipe[i][0]][0]
            cant_cal += recipe[i][1] * dict[recipe[i][0]][1]
        else:
            print(f'{recipe[i][0]} - {recipe[i][1]*dict[recipe[i][0]][1]}')
            num +=1
            cost_rec += recipe[i][1] * dict[recipe[i][0]][0]
            cant_cal += recipe[i][1] * dict[recipe[i][0]][1]
    print(f'\nNumber of ingredients: {num}\n'
          f'Recipe cost: {cost_rec}\n'
          f'Recipe calories: {cant_cal}')

    print()

    in_file3 = open("polenta_concia.txt", "r")
    read_recipe1 = []
    line1 = False
    while line1 != "":
        line1 = in_file3.readline().strip()
        read_recipe1.append(line1)

    read_recipe1.pop(0)
    read_recipe1.pop(-1)

    recipe1 = []
    for line in read_recipe1:
        line = line.split(";")
        info = []
        ing = line[0]
        cant = float(line[1].strip())
        info.append(ing)
        info.append(cant)
        recipe1.append(info)

    # Operation
    first1 = True
    num1 = 0
    cost_rec1 = 0
    cant_cal1 = 0
    for i in range(len(recipe1)):
        if first1:
            print('Ingredients:')
            first1 = False
            print(f'{recipe1[i][0]} - {recipe1[i][1] * dict[recipe1[i][0]][1]}')
            num1 = 1
            cost_rec1 += recipe1[i][1] * dict[recipe1[i][0]][0]
            cant_cal1 += recipe1[i][1] * dict[recipe1[i][0]][1]
        else:
            print(f'{recipe1[i][0]} - {recipe1[i][1] * dict[recipe1[i][0]][1]}')
            num1 += 1
            cost_rec1 += recipe1[i][1] * dict[recipe1[i][0]][0]
            cant_cal1 += recipe1[i][1] * dict[recipe1[i][0]][1]

    print(f'\nNumber of ingredients: {num1}\n'
          f'Recipe cost: {round(cost_rec1,1)}\n'
          f'Recipe calories: {cant_cal1}')

except FileNotFoundError as err:
    print("A file was not found")
except KeyError as err:
    print("There was a recipe written wrong")





in_file1.close()
in_file2.close()
in_file3.close()