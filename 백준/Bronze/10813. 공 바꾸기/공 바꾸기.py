N, M = map(int, input().split())
Box = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    Box[i - 1], Box[j - 1] = Box[j - 1], Box[i - 1]

print(*Box)