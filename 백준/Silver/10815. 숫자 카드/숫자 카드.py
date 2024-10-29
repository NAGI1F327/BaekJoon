N = int(input().strip())
sg_cards = set(map(int, input().strip().split()))

M = int(input().strip())
check_cards = list(map(int, input().strip().split()))

result = []
for card in check_cards:
    if card in sg_cards:
        result.append(1)
    else:
        result.append(0)

print(" ".join(map(str, result)))