text = input("Enter word: ")
print("The compressed text is: ", end="")
lastchar = ""
countoflastchar = 0
for i in range(0, len(text)):
    if text[i] == lastchar:
        countoflastchar += 1
    else:
        if lastchar != "":
            print(f'{lastchar}{countoflastchar}', end="")
        lastchar = text[i]
        countoflastchar = 1
print(f'{lastchar} {countoflastchar}')
