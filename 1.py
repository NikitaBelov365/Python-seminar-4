a = 'a a a b c a a d c d d'

newA = a.split()
dict = {}
result = ''

for i in newA:
    if i not in dict:
        dict[i] = 0
        result = result + i + ' '
        
    else:
        dict[i] += 1
        result = result + (i + '_' + str(dict[i]) + ' ')


print(result)