m, n = map(int, input().split()) #m tipos e n tamanhos
matriz = []
for i in range(m):
    numeros = list(map(int, input().split()))
    matriz.append(numeros)

p = int(input())
c = 0
for __ in range(p):
    i, j = map(int, input().split())
    if matriz[i - 1][j -1] > 0:
        c += 1
        matriz[i - 1][j -1] -= 1

print(c)
