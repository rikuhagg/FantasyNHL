#kokeilu ja opettelua 
import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=False, indent=4)
    print(text)


j = '8478495'

response1 = requests.get('https://statsapi.web.nhl.com/api/v1/people/'+j)
r = json.loads(response1.text)

jprint(r)


response2 = requests.get('https://statsapi.web.nhl.com/api/v1/people/'+j+'/stats?stats=statsSingleSeason&season=20202021')
r2 = json.loads(response2.text)
jprint(response2.json())
        
goals = r2['stats'][0]['splits'][0]['stat']['goals']
assists = r2['stats'][0]['splits'][0]['stat']['assists']
