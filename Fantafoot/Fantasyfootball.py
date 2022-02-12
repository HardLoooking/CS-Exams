
in_file = open("fantafoot.txt", "r")
players = []
for line in in_file:
    line = line.strip()
    element = line.split(",")
    empty_dic = {}
    empty_dic["Name"] = element[0].strip()
    empty_dic["Team"] = element[1].strip()
    empty_dic["Position"] = element[2].strip()
    empty_dic["Price"]  = float(element[3].strip())
    players.append(empty_dic)

#Goalkeepers
budget_gk = 20
i_gk = 0 #Inital Goalkeepers
max_gk = 3 #Max Goalkeepers
avg_gk = round(budget_gk/max_gk,2) #Avg price for goalkeeper
goalkeepers = []
i=0

while i_gk < max_gk:
    if players[i]["Position"] == "portiere" and players[i]["Price"] <= avg_gk:
        budget_gk = budget_gk - players[i]["Price"]
        i_gk += 1
        goalkeepers.append(players[i])
        players.pop(i)
        i += 1
    else:
        players.pop(i)
rest_budget_gk = budget_gk
print(f'Rest budget of Gooalkeepers: {rest_budget_gk} mllls fantaUSD')


#Defenders
budget_def = 40
i_def = 0 #Inital defenders
max_def = 8 #Max defenders
avg_def = round(budget_def/max_def,2) #Avg price for defender
defenders = []
i=0

while i_def < max_def:
    if players[i]["Position"] == "difensore" and players[i]["Price"] <= avg_def:
        budget_def = budget_def - players[i]["Price"]
        i_def += 1
        defenders.append(players[i])
        players.pop(i)
        i += 1
    else:
        players.pop(i)

rest_budget_def = budget_def
print(f'Rest budget of Defenders: {rest_budget_def} mllls fantaUSD')

#Midfielders
budget_mid = 80
i_mid = 0 #Inital midfielders
max_mid = 8 #Max midfielders
avg_mid = round(budget_mid/max_mid,2) #Avg price for midfielders
midfielders = []
i=0

while i_mid < max_mid:
    if players[i]["Position"] == "centrocampista" and players[i]["Price"] <= avg_mid:
        budget_mid = budget_mid - players[i]["Price"]
        i_mid += 1
        midfielders.append(players[i])
        players.pop(i)
        i += 1
    else:
        players.pop(i)


rest_budget_mid = budget_mid
print(f'Rest budget of Midfielders: {rest_budget_mid} mllls fantaUSD')


#Forwards
budget_for = 120
i_for = 0 #Inital Forwards
max_for = 6 #Max Forwards
avg_for = round(budget_for/max_for,2) #Avg price for Forwards
forwards = []
i=0

while i_for < max_for:
    if players[i]["Position"] == "attaccante" and players[i]["Price"] <= avg_for:
        budget_for = budget_for - players[i]["Price"]
        i_for += 1
        forwards.append(players[i])
        players.pop(i)
        i += 1
    else:
        players.pop(i)

rest_budget_for = budget_for
print(f'Rest budget of Forwards: {rest_budget_for} mllls fantaUSD')

print()

"""print(f'Goalkepers: {goalkeepers[0]["Name"]} {goalkeepers[0]["Price"]} {goalkeepers[1]["Name"]} {goalkeepers[1]["Price"]} {goalkeepers[2]["Name"]} {goalkeepers[2]["Price"]}')
print(f'Defenders: {defenders[0]["Name"]} {defenders[0]["Price"]} {defenders[1]["Name"]} {defenders[1]["Price"]} {defenders[2]["Name"]} {defenders[2]["Price"]}'
      f' {defenders[3]["Name"]} {defenders[3]["Price"]} {defenders[4]["Name"]} {defenders[4]["Price"]} {defenders[5]["Name"]} {defenders[5]["Price"]}'
      f' {defenders[6]["Name"]} {defenders[6]["Price"]} {defenders[7]["Name"]} {defenders[7]["Price"]} ')
print(f'Midfielders: {midfielders[0]["Name"]} {midfielders[0]["Price"]} {midfielders[1]["Name"]} {midfielders[1]["Price"]} {midfielders[2]["Name"]} {midfielders[2]["Price"]}'
      f' {midfielders[3]["Name"]} {midfielders[3]["Price"]} {midfielders[4]["Name"]} {midfielders[4]["Price"]} {midfielders[5]["Name"]} {midfielders[5]["Price"]}'
      f' {midfielders[6]["Name"]} {midfielders[6]["Price"]} {midfielders[7]["Name"]} {midfielders[7]["Price"]} ')
print(f'Forwards: {forwards[0]["Name"]} {forwards[0]["Price"]} {forwards[1]["Name"]} {forwards[1]["Price"]} {forwards[2]["Name"]} {forwards[2]["Price"]}'
      f' {forwards[3]["Name"]} {forwards[3]["Price"]} {forwards[4]["Name"]} {forwards[4]["Price"]} {forwards[5]["Name"]} {forwards[5]["Price"]}')"""


for i in range(len(goalkeepers)):
    if i == 0:
        print(f'Goalkepers: {goalkeepers[0]["Name"]} {goalkeepers[0]["Price"]}', end="")
    else:
        print(f' {goalkeepers[i]["Name"]} {goalkeepers[i]["Price"]}', end="")
print()
for i in range(len(defenders)):
    if i == 0:
        print(f'Defenders: {defenders[0]["Name"]} {defenders[0]["Price"]}', end="")
    else:
        print(f' {defenders[i]["Name"]} {defenders[i]["Price"]}', end="")
print()
for i in range(len(midfielders)):
    if i == 0:
        print(f'Midfielders: {midfielders[0]["Name"]} {midfielders[0]["Price"]}', end="")
    else:
        print(f' {midfielders[i]["Name"]} {midfielders[i]["Price"]}', end="")
print()
for i in range(len(forwards)):
    if i == 0:
        print(f'Forwards: {forwards[0]["Name"]} {forwards[0]["Price"]}', end="")
    else:
        print(f' {forwards[i]["Name"]} {forwards[i]["Price"]}', end="")


in_file.close()

