A, B = input().split()

reversed_A = int(A[::-1]) 
reversed_B = int(B[::-1])

if reversed_A > reversed_B:
    print(reversed_A)
else:
    print(reversed_B)