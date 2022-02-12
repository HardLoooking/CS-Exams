def open_arguments():
    try:
        arguments_file = open("arguments.txt", "r")
        arguments_list = arguments_file.read().split("\n")
        arguments_file.close()
    except OSError as err:
        print(err)
    return arguments_list


def open_laws():
    try:
        laws_file = open("Murphy_reads.txt", "r")
        laws_list = laws_file.read().split("\n\n")
        laws_file.close()
    except OSError as err:
        print(err)
    return laws_list


def find_special_laws():
    list_of_answers = []
    for i in range(len(open_laws())):
        for a in open_arguments():
            if (a in open_laws()[i]) and (a not in list_of_answers):
                list_of_answers.append(open_laws()[i])

    return list_of_answers


def print_list(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            if my_list[i][j] == "\n":
                title = my_list[i][:j:]
                statement = my_list[i][j + 1: j + 1 + 50]
                etc = ""
                if len(my_list[i][j + 1:]) > 50:
                    etc = "..."
                print(f"{title} - {statement}{etc}", end="\n\n")
                break


def main():
    print_list(find_special_laws())


if __name__ == "__main__":
    main()
