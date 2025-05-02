n = int(input()) #numero de lances

lances = {}

for i in range(n):
    nome = input()
    valor = int(input())
    lances[nome] = valor

print(max(lances, key=lances.get))
print(max(lances.values()))