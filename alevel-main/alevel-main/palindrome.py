ispalindrome = False
word=''
def restart():
    check = input('do you want to restart Y/N?\n> ').lower()
    if check == 'y':
        palindrome(word)
    if check == 'n':
        return
    else:
        check = input('do you want to restart Y/N? --- ONLY INPUT Y or N for yes or no\n> ').lower()

def palindrome(word):
    word = input('Enter word: ')
    getback = list(word)
    print(getback)
    for i in range(0, len(getback)):
        take = len(word)
        print(take-1-i)
        for x in range(0, len(word)):
            print(f'word i {i}: {word[i]} || word x {x}: {word[x]}')
            if x == i:
                ispalindrome == True
            print(ispalindrome)
    if ispalindrome == True:
        print('Is a palindrome')
    else:
        print('Is not a palindrome')
        restart()
palindrome(word)
