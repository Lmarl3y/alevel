num = int(input('Enter Number: '))

def even(num):
    evennum = []
    if num % 2 == 0:
        evennum.append(num)
        for i in range(num, 0, -2):
            num = num-2
            evennum.append(num)
    if num % 2 != 0:
        num = num-1
        evennum.append(num)
        for i in range(num, 0, -2):
            num = num-2
            evennum.append(num)
    print(evennum)

even(num)
        
