import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=False, indent=4)
    print(text)

def printPlayerName(name):
    print()
    print(name)
    print('='*50)
    
#lue ID:t tiedostosta
file = open('id.txt')
lines = file.readlines();

ids = [] #lista pelaaja ID:stä

for i in lines:
    ids.append(i.strip())

pointsTable = {} #Dictionary kokonaispistetilanteen laskemiseksi

for j in ids:
    if j[0] != '8': #Tarkista onko kyseessä nimi vai ID
        name = j
        pointsTable[j] = 0
        printPlayerName(name)
        
    else:
        peopleInfo = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+j)).text)
        stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+j+'/stats?stats=statsSingleSeason&season=20202021')).text)

        if peopleInfo['people'][0]['primaryPosition']['code'] == 'G':
            print(True)

        elif stats['stats'][0]['splits'] == []:
            goals = 0
            assists = 0
            
        else:     
            goals = stats['stats'][0]['splits'][0]['stat']['goals']
            assists = stats['stats'][0]['splits'][0]['stat']['assists']
            points = goals + assists
            pointsTable[name] += points
            
        print(peopleInfo['people'][0]['fullName'],'| G:',goals, '| A: ',assists, '| P:',(goals+assists))
        
print(pointsTable)
 
