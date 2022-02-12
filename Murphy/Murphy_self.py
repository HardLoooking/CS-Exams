in_file_1 = open("Murphy_reads.txt", "r")
in_file_2 = open("arguments.txt", "r")
#
laws = in_file_1.read().split("\n\n")

words = []
for line in in_file_2:
    line = line.strip()
    words.append(line)

my_list = []
for i in laws:
    for y in words:
        if y in i:
            my_list.append(i)

for law in my_list:
    for y in law:
        if y == "\n":
            num1 = law.index(y)
            law_sen = law[:num1:]
            sentence = law[num1+1:]
            if len(sentence) >= 50:
                etc = "..."
            else:
                etc = ""
            print(f'{law_sen} - {sentence[:50]}{etc} ')




