def mean():
    total = 0
    amount = int(input('Enter amount of numbers you wanna input: '))
    for i in range(amount):
        numbers = int(input('Enter number: '))
        total += numbers
    mean = total/amount
    print(total)
    print(mean)
        
mean()