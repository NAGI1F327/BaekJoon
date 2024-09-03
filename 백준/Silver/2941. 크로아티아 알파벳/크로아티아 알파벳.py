def count_croatia_alphabet(word):
    croatians = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=','z=']
    
    for croatian in croatians:
        word = word.replace(croatian, '!')
        
    return len(word)
        
word = input().strip()
print(count_croatia_alphabet(word))