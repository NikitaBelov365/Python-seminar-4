import random

def ListCreation(length):
    list1 = []
    for i in range(length):
        list1.append(random.randint(0, 10))
    print(list1)
    return list1

list1 = ListCreation(165)

maxNum = 0
i = 0
while list1[i] != 0:
    if maxNum < list1[i]:
        maxNum = list1[i]
    i += 1


print(maxNum)