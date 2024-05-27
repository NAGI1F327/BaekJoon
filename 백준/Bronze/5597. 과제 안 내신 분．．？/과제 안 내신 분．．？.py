submitted = [False] * 30

for _ in range(28):
    number = int(input())
    submitted[number - 1] = True

for i in range(30):
    if not submitted[i]:
        print(i + 1)