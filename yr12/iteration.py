x = int(input('Enter the first integer: '))
y = int(input('Enter the second integer: '))
z = 0
while x > 0:
    if x % 2 == 1:
        z = z+y
    x = x // 2
    y = y*2
print(f'Answer = {z}')