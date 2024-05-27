submitted = [False] * 31

for _ in range(28):
    number = int(input())
    submitted[number] = True

for i in range(1, 31):
    if not submitted[i]:
        print(i)