N, X = map(int, input().split())
N_list = list(map(int, input().split()))

for num in N_list:
    if num < X:
        print(num, end=" ")