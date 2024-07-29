N = int(input().strip())

count = 0
for i in range(1, N + 1):
    digit_sum = sum(int(digit) for digit in str(i))
    
    if digit_sum != 0 and i % digit_sum == 0:
        count += 1

print(count)