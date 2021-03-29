import requests
import json

#hakee pelaajan tiedoista onko kyseinen pelaaja rosterissa vai ei ja tulostaa pelajaat jotka eivät ole aktiivisessa rosterissa
file = open('id2.txt')
lines = file.readlines();
file.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = lines[i].split(';')

    
for ln in lines:
    if (ln[0] != 'p' and ln[0] != 'l' and ln[0] != 'lm') :
        info = json.loads((requests.get('https://statsapi.web.nhl.com/api/v1/people/' + ln[2])).text)

        if(info['people'][0]['rosterStatus'] == 'N'):
            print(info['people'][0]['fullName'])

print()
print('valmis')
