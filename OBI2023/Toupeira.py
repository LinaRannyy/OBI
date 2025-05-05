s, t = map(int, input().split()) #numero de salões e de tuneis

tuneis = []
for i in range(t):
    tu = list(map(int, input().split()))
    tuneis.append(tu)

p = int(input()) # numero de sugestões de passeio
passeios = [] #contém listas com os passeios

for _ in range(p):
    n = list(map(int, input().split()))
    n.remove(n[0])
    passeios.append(n)

possivel = 0 
for passeio in passeios:
    valido = True
    for y in range(len(passeios) - 1):
        par = [passeio[y], passeio[y+1]]
        if par not in tuneis and par[::-1] not in tuneis:
            valido = False
            break
    if valido:
        possivel += 1

print(possivel)