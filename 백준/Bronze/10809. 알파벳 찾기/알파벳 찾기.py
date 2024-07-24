S = input().strip()
position = [-1] * 26

for i in range(len(S)):
    p = ord(S[i]) - ord('a')
    if position[p] == -1:
        position[p] = i

print(' '.join(map(str, position)))