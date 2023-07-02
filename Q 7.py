import random
input_numbers = int(input("how many random numbers do you want: "))

lower_limit = int(input("enter a lower limt : "))
upper_limit = int(input("enter a upper limit : "))
list = []
for i in range (input_numbers ):
    list.append(random.randint(lower_limit, upper_limit))
print("amount inputed", input_numbers)
print(list)

    
 