n = input()
inp = list(n)
count = 1
for x in range(len(inp)):
    case = inp[x].isupper()
    if case == True:
        count = count + 1

print(count)