X = int(input())
N = int(input())

i = 0
while i < N:
    a, b = map(int, input().split())
    X -= a * b
    i += 1

if X == 0:
    print("Yes")
else:
    print("No")