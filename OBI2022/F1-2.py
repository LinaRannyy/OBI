cartas = []
for i in range(7):
    x = input()
    cartas.append(x)

luana = [cartas[1], cartas[2], cartas[3]]
soma_lu = 0
edu = [cartas[4], cartas[5], cartas[6]]
soma_edu = 0

naipes = { "A": 10, "J" : 11, "Q": 12,"K" : 13}

for dom in naipes:
    if cartas[0][0] == dom:
        naipes[dom] += 4

for x in luana:
    soma_lu += naipes[x[0]]
for x in edu:
    soma_edu += naipes[x[0]]

if soma_lu > soma_edu:
    print('Luana')
elif soma_edu == soma_lu:
    print('Empate')
else:
    print('Edu')