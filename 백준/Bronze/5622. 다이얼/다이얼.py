dial_times = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]

word = input().strip()

total_time = 0
for char in word:
    index = ord(char) - ord('A')
    total_time += dial_times[index]

print(total_time)