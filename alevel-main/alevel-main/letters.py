Canbemadefromsecondword = True
Word1 = input('First word, enter ________> ')
Word2 = input('SECOND  word enter ---------~> ')
for Pos in range(0, len(Word1)):
    if Word1[Pos] in Word2:
        Word2 = Word2.replace(Word1[Pos], "", 1)
    else:
        Canbemadefromsecondword = False
if Canbemadefromsecondword:
    print('Yes word in letters ')
else:
    print('nhuh')
