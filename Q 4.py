num1 = int(input("enter a value: "))
num2 = int(input("enter a value: "))
total = 0 
for i in range(num1,num2):
    if i % 2==0:
        print(i , end = " ")
        total = total + i

print( " , sum of all even numbers: " , total)
        
    