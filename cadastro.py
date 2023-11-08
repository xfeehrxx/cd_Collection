import json

art = ''

try:
    with(open('albuns.json', 'r')) as file: 
        data = json.load(file)
except FileNotFoundError:
    data=[]

while art != 'N' and art != 'n':
    b = False
    art = input("Artista:\n").strip()
    alb = input("Album:\n").strip()
    
    for i in range(len(data)):
        if (data[i]['album'] == alb):
            b = True
            break
        
    if (b == False):
        new = {'artista': art, 'album': alb}
        data.append(new)

    with open('albuns.json', 'w') as file:
        json.dump(data, file, indent=4)
    art = input('Cadastrar novo album? (S/N)\n').strip()

print('Encerrado.')