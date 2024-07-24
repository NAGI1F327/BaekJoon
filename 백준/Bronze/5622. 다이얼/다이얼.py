dial_times = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]

word = input().strip()
total_time = sum(dial_times[ord(char) - ord('A')] for char in word)
print(total_time)