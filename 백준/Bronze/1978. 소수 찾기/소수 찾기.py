N = int(input().strip())
numbers = list(map(int, input().split()))

prime_count = 0

for num in numbers:
    if num <= 1:
        continue
    if num <= 3:
        prime_count += 1
        continue
    if num % 2 == 0 or num % 3 == 0:
        continue
    is_prime = True
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            is_prime = False
            break
        i += 6
    if is_prime:
        prime_count += 1

print(prime_count)