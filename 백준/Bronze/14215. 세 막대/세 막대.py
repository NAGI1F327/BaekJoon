a, b, c = map(int, input().split())

while not (a + b > c and a + c > b and b + c > a):
    if a >= b and a >= c:
        a -= 1
    elif b >= a and b >= c:
        b -= 1
    else:
        c -= 1

print(a + b + c)