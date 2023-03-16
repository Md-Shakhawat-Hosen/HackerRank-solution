T = int(input())
for x in range(T):
    n = int(input())
    if n == 0:
        print(1)
    elif n == 1:
        print(1)
    elif n >= 2:
        t = 2
        while t != 0:
            if t == n:
                print(n)
                break
            elif t > n:
                print(t)
                break
            t = 2 * t

