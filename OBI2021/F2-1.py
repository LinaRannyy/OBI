s = int(input())
a = int(input())
b = int(input())

q = 0

def soma(numero):
    n = 0
    novo = str(numero)
    for i in novo:
        n += int(i)
    return n

for i in range(a, b + 1):
    if soma(i) == s:
        q += 1

print(q)