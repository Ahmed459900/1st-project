a = int(input("enter number: "))
b = int(input("enter number: "))
c = int(input("enter number: "))
d = int(input("enter number: "))
e = int(input("enter number: "))
f = int(input("enter number: "))
g = int(input("enter number: "))
h = int(input("enter number: "))

list = []
list.append(a)   ## Use append() to add elements
list.append(b)
list.append(c)
list.append(d)
list.append(e)
list.append(f)   ## Use append() to add elements
list.append(g)
list.append(h)

list.sort()
print(list)
print("The youngest employee is : ", list[0])

print("The oldest employee is:" , list[7])
