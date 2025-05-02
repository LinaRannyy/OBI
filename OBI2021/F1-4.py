n = int(input())
vazio = []
for i in range(n):
    v = int(input())

    if v == 0 and vazio:
        vazio.pop()
    else:
        vazio.append(v)
        


print(sum(vazio))
