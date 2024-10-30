N, M = map(int, input().split())
S = set(input().strip() for _ in range(N))
ck_str = [input().strip() for _ in range(M)]

cnt = 0
for string in ck_str:
    if string in S:
        cnt += 1

print(cnt)