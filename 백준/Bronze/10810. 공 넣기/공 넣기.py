N, M = map(int, input().split())

Box = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for b in range(i - 1, j):
        Box[b] = k

print(" ".join(map(str, Box)))