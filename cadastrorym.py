from bs4 import BeautifulSoup
import requests
import json

hsr= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}

name = input('Nick:\n')
data = []

def cadastro(p):
    page = requests.get('https://rateyourmusic.com/collection/Remul0/oo/ '+ str(p), headers=hsr)
    page = BeautifulSoup(page.content, 'html.parser')
    cd = page.find_all("div", class_='or_q_albumartist')

    for i in range(len(cd)):
        art = cd[i].find('a', class_='artist').text
        alb = cd[i].find('a', class_='album').text
        new = {'artista': art, 'album': alb}
        data.append(new)

    with open(name +'.json', 'w') as file:
        json.dump(data, file, indent=4)
    if (p == ''):
        qty = page.find_all('a', class_="navlinknum")
        return qty

qty = cadastro('')
for i in range(1, len(qty)):
    if(qty[i].text < qty[i-1].text):
        del qty[i:]
        break
    else:
        cadastro(str(qty[i].text))

