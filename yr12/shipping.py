ordertotal = float(input("Enter money price total: £"))
newprice = 0
if ordertotal < 15:
    newprice = ordertotal + 3.5

nextday = input("Would you like next day delivery? (+£5)\n Y/N: ")
if nextday == "T":
    finalprice = newprice + 5
    print(f'Order total: £{finalprice}')
else:
    finalprice = newprice
    print(f'Order total: £{finalprice}')
