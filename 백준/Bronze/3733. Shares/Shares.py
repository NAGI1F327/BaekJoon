data = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        data.extend(line.split())
    except EOFError:
        break

i = 0
while i < len(data):
    N = int(data[i])
    S = int(data[i + 1])
    x = S // (N + 1)
    print(x)
    i += 2