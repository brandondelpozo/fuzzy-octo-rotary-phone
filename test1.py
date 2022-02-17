""" # from team international
Giving the following string by team international
sample = "aaabbbccbacdeb"

Print the 3 most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.

Note: order by letter if the number repeats

The sample output would be:
b : 5
a : 4
c : 3
"""

"""
Pseudocode
declare string
empty_string
count = 0
count_element = 0

for each element in string
if element1 is already in empty string
count + 1
if element1 is not in empty string
add it
after finish it go to element2
count_element+=1

"""

#sample = "aaabbb"


def count_char(sample):
    new_string = " "
    count = 0
    for e in sample:
        if e in new_string:
            count+=1
        else:
            new_string+=e
    print(new_string, count)

count_char("aaaaabb")