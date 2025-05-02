n = []
for i in range(5):
    x = int(input())
    n.append(x)

trofeus = 0
placas = 0
menores = []

for i in n:
    if i < n[0]:
        menores.append(i)

for y in n:
    if y == n[0]:
        trofeus += 1
    if y in menores and y == menores[0]:
        placas += 1

print(trofeus, placas)