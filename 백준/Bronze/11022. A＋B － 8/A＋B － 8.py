T = int(input())

i = 1
while i <= T:
    A, B = map(int, input().split())
    print(f"Case #{i}: {A} + {B} = {A + B}")
    i += 1