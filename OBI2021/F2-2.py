monica = int(input())
f1 = int(input())
f2 = int(input())

f3 = monica - (f1 + f2)

if f3 > f2 and f3 > f1:
    print(f3)
elif f2 > f3 and f2 > f1:
    print(f2)
else:
    print(f1)