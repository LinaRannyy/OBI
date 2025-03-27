a = int(input())
b = int(input())
c = int(input())


if b > c > a  or a > c > b:
    print(c)
elif c > b > a  or a > b > c:
    print(b)
elif b > a > c  or c > a > b:
    print(a)
elif b == a or b == c:
    print(b)
else:
    print(a)
    