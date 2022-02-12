dictionary = {}
try:
    with open("glucometer.txt", "r") as infile:
        for line in infile:
            line = line.strip()
            line = line.split()
            for i in range(len(line)):
                if line[i].isdigit():
                    line[i] = int(line[i])
            if line[0] not in dictionary:
                dictionary[line[0]] = []
            name = line[0]
            line.pop(0)
            dictionary[name].append(line)
        print(dictionary)
        aux_dictionary = {}
        for element in dictionary:
            aux_dictionary[element] = 0
            for thing in dictionary[element]:
                if thing[1] >= 200:
                    aux_dictionary[element] += 1
            if aux_dictionary[element] == 0:
                aux_dictionary.pop(element)
        while len(aux_dictionary) != 0:
            counter = 0
            maximum = ""
            for element in aux_dictionary:
                if aux_dictionary[element] > counter:
                    counter = aux_dictionary[element]
                    maximum = element
            for element in dictionary[maximum]:
                if element[1] >= 200:
                    print(maximum, element[0], element[1])
            dictionary.pop(maximum)
            aux_dictionary.pop(maximum)
            print()
except OSError as error:
    print(error)