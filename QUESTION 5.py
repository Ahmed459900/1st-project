a = [23, 89, 90, 23, 23 ,78, 89, 45, 11, 8, 1, 56, 34, 78, 40, 21]
output =[]
for i in a:
    if i not in output:
        output.append(i)
        
print(output)