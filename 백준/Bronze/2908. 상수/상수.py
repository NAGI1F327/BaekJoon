A, B = input().split()

reversed_A = int(A[2] + A[1] + A[0])
reversed_B = int(B[2] + B[1] + B[0])

if reversed_A > reversed_B:
    print(reversed_A)
else:
    print(reversed_B)