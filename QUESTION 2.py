import math
a = int(input("enter number: "))
b = int(input("enter number: "))
c = int(input("enter number: "))
d = int(input("enter number: "))
e = int(input("enter number: "))
user_input = [a , b, c, d, e]
list = []          ## Start as the empty list
list.append(a**2)   ## Use append() to add elements
list.append(b**2)
list.append(c**2)
list.append(d**2)
list.append(e**2)
print (user_input)
print(list)
