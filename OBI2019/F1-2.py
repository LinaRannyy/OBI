n = int(input())
seq = []
for i in range(n):
    new = int(input())
    seq.append(new)

numero = []

for x in range(0, len(seq) - 1):  
  if seq[x] != seq[x + 1] and seq.count(seq[x]) > 1:
     if seq[x] not in numero and len(numero) < 2:
       numero.append(seq[x])
  elif len(seq) < 2:
     numero.append(seq[x])

print(len(numero))