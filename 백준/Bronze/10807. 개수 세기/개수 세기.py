N = int(input())
N_list = list(map(int, input().split()))   # N개 정수 리스트
v = int(input())

count = N_list.count(v)
print(count)