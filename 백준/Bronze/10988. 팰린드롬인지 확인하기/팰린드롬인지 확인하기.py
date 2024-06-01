word = input().strip()
length = len(word)
palindrome = 1

for i in range(length // 2):
    if word[i] != word[length - i - 1]:
        palindrome = 0
        break

print(palindrome)