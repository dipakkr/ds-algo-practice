a = []

x = input()

L = list(x)

length = len(L)

for i in range(length-1, 0, -1):
    a.append(L[i])
    
a.append(L[0])

for i in range(length):

    for j in range(length - 1):

        if i != j:
           a.append(L[j] + L[i])

print(a)


c =[]

for i in range(length):
    for j in range(length):
        c.append()


