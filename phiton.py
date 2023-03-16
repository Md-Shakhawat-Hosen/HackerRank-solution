a,b = map(int,input().split())
if a > b:
    print("Argentina")
elif a < b:
    print("Brazil")
else:
    s1 = input()[:5]
    s2 = input()[:5]
    x = s1.count('1')
    y = s2.count('1')
    while x == y:
        s1 = input()[:5]
        s2 = input()[:5]
        x = s1.count('1')
        y = s2.count('1')
    if x > y:
        print("Argentina")
    else:
        print("Brazil")