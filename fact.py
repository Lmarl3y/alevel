num  = int(input('Enter a number: '))
total = num
for i in range(num-1, 0, -1):
    total = total*i
print(total)
