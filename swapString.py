
def findCase(s):
    li = list(s.split(' '))
    l = li[::-1]
    st = ""
    for i in range(len(l)):
        for j in range(len(l[i])):
            ch = l[i][j]
            if ch.islower():
                #print(l[i][j].upper(), end="")
                st = st + l[i][j].upper()
            else:
                #print(l[i][j].lower(), end="")
                st = st + l[i][j].lower()
        st = st + " "
    return st

s = "aWESOME is cODING"
r = findCase(s)
print(r)