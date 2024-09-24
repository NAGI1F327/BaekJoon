N_list = [int(input()) for _ in range(9)]

max_value = max(N_list)
max_index = N_list.index(max_value) + 1

print(max_value)
print(max_index)