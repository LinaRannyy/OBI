n = int(input())
a = int(input()) #açougue
f = int(input()) #farmácia
p = int(input()) #padaria

contas = [a, f, p]
c = 0

for i in contas:
    if n >= i:
        n -= i
        c += 1

print(c)