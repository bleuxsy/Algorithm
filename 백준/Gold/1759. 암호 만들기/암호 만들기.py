from itertools import combinations
L , C = map(int, input().split())
alphabets = input().split()
pw = combinations(sorted(alphabets),L)

for password in pw:
    vowel = 0
    consonant = 0
    for word in password:
        if word in 'aeiou':
            vowel += 1
        else: consonant +=1
    if vowel >= 1 and consonant>=2:
        print("".join(password))