S = input().strip()
position = [-1] * 26

for i in range(len(S)):
    p = ord(S[i]) - ord('a')
    # ord : 단일 문자 유니코드 코드 포인트 반환
    if position[p] == -1:
        position[p] = i

print(' '.join(map(str, position)))