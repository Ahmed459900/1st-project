import random 
def pinGenerator():
    list = []
    n = int(input("how many passwords: "))
    for i in range(n):
        upper_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&^*()_+"
        combination  = (upper_alphabets + numbers + symbols)
        password = (random.choices(upper_alphabets, k=4) +
                    random.choices(numbers, k=4) +
                    random.choices(symbols, k=2))
        random.shuffle(password[0:4])
        random.shuffle(password[4:8])
        random.shuffle(password[8:])
        list.append("".join(password))
    print(list)
        

       
pinGenerator()

