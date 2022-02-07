
"""
def count_words():
    phrase = input("Insert a new phrase: ")
    new_list = phrase.split(" ")
    nl_count = len(new_list)
    print(nl_count)

count_words()
"""
# Other way to solve the same problem
phrase = input("Insert a new phrase: ")
count = 0

for char in phrase:
    if char == ' ':
        count += 1
    else:
        continue

count = count + 1
print(count)