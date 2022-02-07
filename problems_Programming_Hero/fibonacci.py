"""
pseudocode
declare element 1
declare element 2
declare an empty list
the funcion take element 1 and element 2
    insert those elements into a list
    sum both element
    append the sum
    repeat the logic until the infinite

call the function
"""



def fibo(e1, e2):
    i = 0
    y = 1
    list = [e1, e2]
    while len(list) < 10:
        sum = list[i] + list[y]
        list.append(sum)
        print(list)
        i+=1
        y+=1

fibo(1, 2)
# test to git