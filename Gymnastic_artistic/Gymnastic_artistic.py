"""
- Read file
- Strip file
-Separate by spaces
- Save each information for each player ( Name, sex, country)
- Operate the scores
    - Remove max and min value
    - Sum of the rest
    -save sum
- List of dictionaries at the end
"""
participants = []
try:
    infile = open("scores.txt", "r")
    for element in infile:
        line = element.strip()
        player = line.split(" ") #Print the list of data
        dict_player = {}
        dict_player["Name"] = player[0] + " " + player[1]
        dict_player["Sex"]= player[2]
        dict_player["Country"]=player[3]
        score_player = []
        for y in range(4,len(player)):
            score_player.append(float(player[y]))
        score_player.remove(max(score_player))
        score_player.remove(min(score_player))
        final_score = sum(score_player)
        dict_player["Score"] = round(final_score,1)
        participants.append(dict_player)

    # The best female player
    max_1 = 0
    for i in range(0,len(participants)):
        if participants[i]["Sex"] == "F":
            if participants[i]["Score"] > max_1:
                max_1 = participants[i]["Score"]
                ind_1 = i

    print(f'Female winner:\n{participants[ind_1]["Name"]},'
          f' {participants[ind_1]["Country"]}'
          f' - Score: {participants[ind_1]["Score"]}')

    print()

    c_scores = []
    c_countries = [] #Will save scores of each country
    count_ita =0
    count_eng =0
    count_rus =0
    count_usa =0
    count_grb =0

    for i in participants:
        if i["Country"] == "ITA":
            count_ita = count_ita + i["Score"]
        elif i["Country"] == "ENG":
            count_eng = count_eng + i["Score"]
        elif i["Country"] == "RUS":
            count_rus = count_rus + i["Score"]
        elif i["Country"] == "USA":
            count_usa = count_usa + i["Score"]
        elif i["Country"] == "GRB":
            count_grb = count_grb + i["Score"]
    c_scores.append(count_ita)
    c_countries.append("ITA")
    c_scores.append(count_eng)
    c_countries.append("ENG")
    c_scores.append(count_rus)
    c_countries.append("ENG")
    c_scores.append(count_usa)
    c_countries.append("USA")
    c_scores.append(count_grb)
    c_countries.append("GRB")

    z = 1
    print(f'Overall nations ranking: ')
    while z < 4 :
        max_1 = max(c_scores)
        ind_1 = c_scores.index(max_1)
        print(f'{z}) {c_countries[ind_1]} - Final score: {c_scores[ind_1]}')
        c_scores.remove(max_1)
        c_countries.pop(ind_1)
        z += 1
except FileNotFoundError as a:
    print("File not found, enter a right address!")

else:
    infile.close()
finally:
    print("Program executed")