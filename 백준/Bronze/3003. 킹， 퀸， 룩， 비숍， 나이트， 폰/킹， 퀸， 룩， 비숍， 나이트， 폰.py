require = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().strip().split()))

result = []
for i in range(len(require)):
    result.append(require[i] - found[i])

print(" ".join(map(str, result)))