n = int(input())
lista = []
for i in range(n):
    v = int(input())
    lista.append(v)

seq = []
for i in lista:
    c = lista.count(i)
    if c > 1:
        seq.append(i)

if n == 1:
    seq.append(lista[0])

seqfinal = []
if len(seq) == 1:
    seqfinal.append(seq[0])
else:
    for i in range(len(seq) - 1):
        if seq[i] != seq[i + 1]:
            seqfinal.append(i)

print(len(seqfinal))

#quantidade máxima de numeros que podem ser marcados com um círculo
#não contenha 2 numeros iguais consecutivos, a sequencia dos marcados
#no max 2 numeros distintos

