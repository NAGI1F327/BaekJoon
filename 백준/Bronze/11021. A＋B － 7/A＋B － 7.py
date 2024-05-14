N = int(input())

i = 1
while i <= N:
    A, B = map(int, input().split())
    print("Case #", i, ": ", A + B, sep="")
    i += 1