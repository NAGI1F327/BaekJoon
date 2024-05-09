N = int(input())

i = 1
mul = 1
while i <= 9:
    mul = N * i
    i = i + 1
    print(N, "*", i-1, "=", mul)