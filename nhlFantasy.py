import requests
import json



def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=False, indent=4)
    print(text)
    

file = open('id.txt')

lines = file.readlines();
ids = []

for i in lines:
    ids.append(i.strip())

pointsTable = {}

for j in ids:
    if j[0] != '8':
        player = j
        pointsTable[j] = 0
        
        print()
        print(j)
        print('='*50)
    else:
        
        peopleInfo = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+j)).text)
        stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+j+'/stats?stats=statsSingleSeason&season=20202021')).text)

        if stats['stats'][0]['splits'] == []:
            goals = 0
            assists = 0
        else:     
            goals = stats['stats'][0]['splits'][0]['stat']['goals']
            assists = stats['stats'][0]['splits'][0]['stat']['assists']
            points = goals + assists
            pointsTable[player] += points
        print(peopleInfo['people'][0]['fullName'],'| G:',goals, '| A: ',assists, '| P:',(goals+assists))
print(pointsTable)
 
