def frequent_letter(word):
    frq = [0] * 26
    word = word.lower()
    
    for char in word:
        index = ord(char) - ord('a')
        frq[index] += 1
        
    max_frq_cnt = max(frq)
    max_frq_letter = []
    
    for i in range(26):
        if frq[i] == max_frq_cnt:
            max_frq_letter.append(chr(i + ord('a')))
    
    if len(max_frq_letter) > 1:
        return '?'
    else:
        return max_frq_letter[0].upper()
        
word = input().strip()
result = frequent_letter(word)
print(result)