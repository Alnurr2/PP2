vowels = "aeiou"
cnt = 0
n = input("")
for vowel in n:
    if vowel in vowels:
        cnt+=1

print(cnt)