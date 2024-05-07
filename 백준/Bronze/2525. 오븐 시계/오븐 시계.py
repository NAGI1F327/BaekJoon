H, M = map(int, input().split())
m = int(input())
H += m // 60
M += m % 60

if M >= 60: 
	H += 1
	M -= 60

if H >= 24:
	H -= 24
    
print(H, M)