

def split_and_join(s):
    output = ''
    for char in s:
        if char == ' ':
            output = output + '-'
        else:
            output = output + char

    return output



n = input()
result = split_and_join(n)
print(result)