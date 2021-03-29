import requests
import json
import time

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=False, indent=4)
    print(text)

def printPlayerName(name):
    print()
    print(name)
    print('='*50)

def pelaaja(Id,pointsTable):
    peopleInfo = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+Id)).text) #lataa pelajaan tiedot apista
    stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+Id+'/stats?stats=statsSingleSeason&season=20202021')).text)

    if peopleInfo['people'][0]['primaryPosition']['code'] == 'G': #tarkistaa onko kyseessä maalivahti
        maalivahti(Id,pointsTable,peopleInfo,stats)

    else:
        if stats['stats'][0]['splits'] == []: 
            goals = 0
            assists = 0
            
        else:     
            goals = stats['stats'][0]['splits'][0]['stat']['goals']
            assists = stats['stats'][0]['splits'][0]['stat']['assists']
            points = goals + assists
            pointsTable[name] += points
            
        print(peopleInfo['people'][0]['fullName'],'| G:',goals, '| A: ',assists, '| P:',(goals+assists))
            

def maalivahti(Id,pointsTable,peopleInfo,stats):
    goals = 0
    assists = 0
    wins = stats['stats'][0]['splits'][0]['stat']['wins']
    shutOuts = stats['stats'][0]['splits'][0]['stat']['shutouts']*2
    pointsTable[name] += wins+shutOuts
    print(peopleInfo['people'][0]['fullName'],'| W:',wins, '| SO: ',shutOuts, '| P:',(wins+shutOuts))

    #Loppupisteytyksessä saatavat pisteet
    svProsentti = stats['stats'][0]['splits'][0]['stat']['savePercentage']*100
    gaa = stats['stats'][0]['splits'][0]['stat']['goalAgainstAverage']
    loppupisteet = (svProsentti/gaa)/1.5
    print(loppupisteet)
    
    
alku = time.time()  
#lue ID:t tiedostosta
file = open('id.txt')
lines = file.readlines();
file.close

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
        pelaaja(j,pointsTable)
        
        
print()
print(pointsTable) #tulostaa sen hetkisenkokonaispistetilanteen
print(time.time() - alku)
