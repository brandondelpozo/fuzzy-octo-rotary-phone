"""
word = 'asfidue'
count = 0

for letter in word:
    if letter == 'a':
        count+=1
    elif letter == 'e':
        count+=1
    elif letter == 'i':
        count+=1
    elif letter == 'o':
        count+=1
    elif letter =='u':
        count+=1
    else:
        continue
print(count)
"""

# Another way to solve the problem
"""
word = "abcdwefio"
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for letter in word:
    for vowel in vowels:
        if letter == vowel:
            count+=1
print(count)
"""

# Another way to solve the problem with functions

def count_vowels(word):
    #word = input("Enter a word: ")
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    count = 0
    for letter in word:
        for vowel in vowels:
            if letter == vowel:
                count+=1
    print(count)

count_vowels("abcdEdI")