""" from team international
Giving two words please provide a list in alphabetical order of common characters found in both words, please avoid using nested loops
Sample input:
word_1 = 'maria'
word_2 = 'marcela'

 The sample output would be:
['a', 'm', 'r']
"""
word_1 = 'mariaa'
word_2 = 'marcela'
n_list = []

for e in word_1:
    if e not in word_2:
        pass
    elif e in n_list:
        pass
    else:
        n_list+=e

print(n_list)