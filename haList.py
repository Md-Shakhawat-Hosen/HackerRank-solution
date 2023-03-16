
n = int(input())
li = []
for x in range(1,n+1):
    st = input().split()
    if len(st) == 3:
        s = st[0]
        index = int(st[1])
        val = int(st[2])
    elif len(st) == 2:
        s = st[0]
        val = int(st[1])
    else:
        s = st[0]
    if s == 'insert':
        li.insert(index,val)
    elif s == 'remove':
        li.remove(val)
    elif s == 'append':
        li.append(val)
    elif s == 'print':
        print(li)
    elif s == 'pop':
        if len(li) > 0:
            li.pop()
    elif s == 'reverse':
        li.reverse()
    elif s == 'sort':
        li.sort()
