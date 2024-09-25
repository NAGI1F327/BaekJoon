numbers = []

for _ in range(10):
    num = int(input())
    numbers.append(num)

remainders = set()

for number in numbers:
    remainder = number % 42
    remainders.add(remainder)

print(len(remainders))