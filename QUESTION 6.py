
a = 1
while True:
    Number = int(input('Enter a number 0 to number you want to stop.. '))
    if Number == 0:
        break
    a = a * Number

print('Product of all numbers You entered..', a)
