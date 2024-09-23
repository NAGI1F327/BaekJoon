import sys

T = int(input())

i = 0
while i < T:
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A + B)
    i += 1