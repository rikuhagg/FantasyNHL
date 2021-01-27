import requests
import json

f = open('ids.txt','a')
og = open('id.txt','r')

lines = og.readlines()
og.close()

ids = []
for j in lines:
    ids.append(j.strip())

for i in ids:
    info = stats = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/'+i)).text)
    f.write('a'+';'+(info['people'][0]['fullName'])+';'+i+'\n')

f.close()
