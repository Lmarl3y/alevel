def workout():
    num = int(input("Enter number: "))

    while num <= 1:
        num = int(input("Enter number greater than 1: "))
    if num % 2 != 0:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')
    cont = int(input('\nWould you like to:\n1. Continue with a new number\n2. Stop here\n\nOption (1, 2): '))
    while cont == 1:
        workout()

workout()