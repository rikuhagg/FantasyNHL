import requests
import json

def p(ln):
    print()
    print(ln[1])
    print('='*50)


def maalit(ln): #Alkuperäinen pelaaja
    stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+ln[2]+'/stats?stats=statsSingleSeason&season=20212022')).text)
    if stats['stats'][0]['splits'] == []: 
            goals = 0
    else:
        goals = stats['stats'][0]['splits'][0]['stat']['goals']
    print(goals)

def syotot(ln):
    stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+ln[2]+'/stats?stats=statsSingleSeason&season=20212022')).text)
    if stats['stats'][0]['splits'] == []: 
            assists = 0
    else:
        assists = stats['stats'][0]['splits'][0]['stat']['assists']  
    print(assists)

def voitot(ln): #Maalivahti
    stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+ln[2]+'/stats?stats=statsSingleSeason&season=20212022')).text)
    if stats['stats'][0]['splits'] == []: 
            wins = 0
    else:
        wins = int(stats['stats'][0]['splits'][0]['stat']['wins'])
    print(wins)

def so(ln): #Maalivahti
    stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+ln[2]+'/stats?stats=statsSingleSeason&season=20212022')).text)
    if stats['stats'][0]['splits'] == []: 
            so = 0
    else:
        so = int(stats['stats'][0]['splits'][0]['stat']['shutouts'])*2
    print(so)

#lue ID:t tiedostosta
file = open('2122pelaajat.txt')
lines = file.readlines();
file.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = lines[i].split(';')

pointsTable = {} #Dictionary kokonaispistetilanteen laskemiseksi

for i in lines:
    if i[0] == 'p':
        player = p(i)   
    if i[0] == 'a':
        maalit(i)
    if i[0] == 'g':
        voitot(i)

print('='*50)

for i in lines:
    if i[0] == 'p':
        player = p(i)   
    if i[0] == 'a':
        syotot(i)
    if i[0] == 'g':
        so(i)
        
   
    
print()
print(pointsTable) #tulostaa sen hetkisenkokonaispistetilanteen
 




