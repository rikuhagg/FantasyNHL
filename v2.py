import requests
import json

def p(ln,pointsTable):
    print()
    print(ln[1])
    print('='*50)
    pointsTable[ln[1]] = 0
    return ln[1]

def a(ln,pointsTable,player):
    stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+ln[2]+'/stats?stats=statsSingleSeason&season=20202021')).text)
    if stats['stats'][0]['splits'] == []: 
            goals = 0
            assists = 0
    else:
        goals = stats['stats'][0]['splits'][0]['stat']['goals']
        assists = stats['stats'][0]['splits'][0]['stat']['assists']
        
    points = goals + assists
    pointsTable[player] += points
    print(ln[1],'| G:',goals, '| A: ',assists, '| P:',points)
    
def l(ln,PointsTable,player):
    goals = ln[3]
    assists = ln[4]
    points = int(goals)+int(assists)
    pointsTable[player] += points
    print(ln[1],'| G:',goals, '| A: ',assists, '| P:',points,'LUKITTU')

def v(ln,pointsTable,player):
    stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+ln[2]+'/stats?stats=statsSingleSeason&season=20202021')).text)
    goals = int(stats['stats'][0]['splits'][0]['stat']['goals']) - int(ln[3])
    assists = int(stats['stats'][0]['splits'][0]['stat']['assists']) - int(ln[4])
    points = int(goals)+int(assists)
    pointsTable[player] += points
    print(ln[1],'| G:',goals, '| A: ',assists, '| P:',points)
    
def g(ln,pointsTable,player):
    stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+ln[2]+'/stats?stats=statsSingleSeason&season=20202021')).text)
    wins = int(stats['stats'][0]['splits'][0]['stat']['wins'])
    so = int(stats['stats'][0]['splits'][0]['stat']['shutouts'])*2
    pointsTable[player] += so + wins

    print(ln[1],'| W:',wins, '| SO: ',so, '| P:',(wins+so))

def lm(ln,pointsTable,player):
    wins = ln[3]
    so = ln[4]
    points = int(wins) + int(so)
    pointsTable[player] += points
    print(ln[1],'| W:',wins, '| SO: ',so, '| P:',points,'LUKITTU')

def vm(ln,pointsTable,player):
    stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+ln[2]+'/stats?stats=statsSingleSeason&season=20202021')).text)
    wins = int(stats['stats'][0]['splits'][0]['stat']['wins']) - int(ln[3])
    so = int(stats['stats'][0]['splits'][0]['stat']['shutouts'])*2 - int(ln[4])
    points = wins + so
    pointsTable[player] += points
    print(ln[1],'| W:',wins, '| SO: ',so, '| P:',(points))
    
    
#lue ID:t tiedostosta
file = open('id2.txt')
lines = file.readlines();
file.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = lines[i].split(';')

pointsTable = {} #Dictionary kokonaispistetilanteen laskemiseksi

for i in lines:
    if i[0] == 'p':
        player = p(i,pointsTable)
        
    if i[0] == 'a':
        a(i,pointsTable,player)

    if i[0] == 'l':
        l(i,pointsTable,player)

    if i[0] == 'v':
        v(i,pointsTable,player)

    if i[0] == 'g':
        g(i,pointsTable,player)
        
    if i[0] == 'lm':
        lm(i,pointsTable,player)

    if i[0] == 'vm':
        vm(i,pointsTable,player)
        
    
print()
print(pointsTable) #tulostaa sen hetkisenkokonaispistetilanteen
 




