# psuedocode
"""
declare list 1
declare list 2 empty
for each element in list 1 
choose an element
    if the element chosen is already inside list2 drop it
    if the element chosen is not in list 2 put it into list 2
return list 2
"""

list = "aba"
list2 = " "

for letter in list:
    if letter in list2:
        pass
    else:
        list2 = list2 + letter

print(list2)
