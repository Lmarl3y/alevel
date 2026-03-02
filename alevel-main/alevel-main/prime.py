def number():
    global score
    score = 0
    number = int(input("Enter a random real number "))
    while number <= 1:
        print("number not greater than 1")
        number = int(input("Enter a random real number "))
    numb = pow(number, 0.5)
    if numb % 1 == 0:
        score +=1
    if number % 2 != 0:
        score +=0
    if score > 0:
        print("is not prime")
    else:
        print("is prime")
    number2()    

def number2():
    global score
    number2 = input("would you like to enter a second number? ").lower()
    score = 0
    if number2 == "yes" or number2 == "y":
        score = 1
    else:
        score = 0
    while score > 0:
        number()      
   
number()
number2()
