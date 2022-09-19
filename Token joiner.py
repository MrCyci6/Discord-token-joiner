# Discord token joiner V1.0.0
# by MrCyci6#0001

import requests
import time

url = input("Lien >> ")
invite = url.split("/")[-1]

with open("tokens.txt", "r") as fd:
    lines = fd.read().splitlines()
length = len(lines)

nbr = 0
for i in range(length):
    time.sleep(1)

    x = lines[i]

    authorization_token = x

    api_invite_url = "https://discord.com/api/v10/invites/" + invite

    try: 
        response = requests.post(api_invite_url, headers={"Authorization": authorization_token})

        if response.ok:
            nbr += 1
            print(f"Successfull join : {nbr}")
        else:
            print(f"Erreur: {response.text}")
    except:
        pass
print(f'{nbr} joins')