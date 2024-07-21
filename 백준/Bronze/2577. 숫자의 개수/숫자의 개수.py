A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result_str = str(result)

digit_count = [0] * 10
# = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for char in result_str:
    digit_count[int(char)] += 1

for count in digit_count:
    print(count)