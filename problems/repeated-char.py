a = 'abcc'

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
     't', 'u', 'v', 'w', 'x', 'y', 'z']

y = list(a)
t =[]

for i in range(len(a)):

    if a[i] not in t:
        t.append(a[i])
    else:
        print(a[i])
