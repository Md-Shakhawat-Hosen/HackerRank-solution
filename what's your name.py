



# def print_full_name(firstName, lastName):
#     print(f'Hello {firstName} {lastName}! You just delved into python.')
#
#
#
# first = input()
# last = input()
# print_full_name(first,last)

s = 'arunununghhjj'
sb = 'nun'
results = 0
sub_len = len(sb)
for i in range(len(s)):
    if s[i:i+sub_len] == sb:
        results += 1
print (results)