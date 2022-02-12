import operator

def Main():

    in_file1 = open("players.csv","r")
    in_file2 = open("games.csv", "r")

    header1 = next(in_file1)
    header2 = next(in_file2)

    #Players
    players = {}
    for line in in_file1:       #PLAYER,SELO
        line= line.strip()
        line= line.split(",")
        name = line[0].strip()
        SELO = int(line[1].strip())
        players[name]=SELO


    #Games
    matches = []
    for line in in_file2:       #PLAYER A,PLAYER B,RESULT
        line= line.strip()
        line=line.split(",")
        match = []
        pA = line[0].strip()  #Player A
        pB = line[1].strip()  #Player B
        result = line[2].strip().split("-")
        if "/" in result[0]:
            result[0] = result[0].split("/")
            A1 = int(result[0][0])
            A2 = int(result[0][1])
            rA = A1/A2
        else:
            rA= int(result[0]) #Result player A
        if "/" in result[1]:
            result[1] = result[1].split("/")
            B1 = int(result[1][0])
            B2 = int(result[1][1])
            rB = B1/B2
        else:
            rB= int(result[1]) #Result player B
        match.append(pA)
        match.append(pB)
        match.append(rA)
        match.append(rB)
        matches.append(match)



    for i in range(len(matches)):
        playerA = matches[i][0]
        playerB = matches[i][1]
        if playerA not in players:
            players[playerA] = 1500
            SELOA = 1500
        else:
            SELOA = players[playerA]
        if playerB not in players:
            players[playerB] = 1500
            SELOB = 1500
        else:
            SELOB = players[playerB]
        delta_match = delta(SELOA, SELOB)
        if matches[i][2] > matches[i][3]:
            SELOA = SELOA +200*delta_match
            SELOB = SELOB -200*delta_match
        elif matches[i][2] < matches[i][3]:
            SELOA = SELOA -200*delta_match
            SELOB = SELOB +200*delta_match
        players[playerA] = round(SELOA)
        players[playerB] = round(SELOB)

    playersR = sorted(players.items(), key=operator.itemgetter(1), reverse=True)
    for k, v in playersR:
        print(f'{k}: {v}')

    in_file1.close()
    in_file2.close()

def delta(player_1, player_2):
    a = 1 / (1 + 2 ** ((player_1 - player_2) / 100))
    return a

Main()

