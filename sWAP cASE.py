



def swapfun(s):
    output = ''
    for char in s:
        if (char.isupper() == True):
            output = output + (char.lower())
        elif char.islower() == True:
            output = output + char.upper()
        else:
            output = output + char

    return output




n = input()
new = swapfun(n)
print(new)




