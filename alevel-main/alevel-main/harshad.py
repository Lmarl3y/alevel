isHarshad = False
start = 1
numbersSoFar = 0
HarshadNum = 1
num = 0
total = 0
numbersSoFar = 0
def isitharshad(num, total, numbersSoFar):
    num = int(input('num: '))
    while numbersSoFar != num:
        Sum = 0
        listit = list(map(int, str(start)))
        total = sum(listit)
        for i in range(0, total):
            Sum += total
        if HarshadNum % Sum == 0:
            numbersSoFar += 1
            if numbersSoFar == num:
                print(HarshadNum)
        HarshadNumber += 1

isitharshad(num, total, numbersSoFar)
        

