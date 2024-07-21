T = int(input())

for _ in range(T):
    quiz = input().strip()
    score = 0
    O = 0
    
    for char in quiz:
        if char == 'O':
            O += 1
            score += O
        else:
            O = 0
    
    print(score)