t = int(input())

for i in range(t):

    n = int(input())
    x = input()
    x = x.split(' ')

    dict = {}

    for i in x:

        keys = dict.keys()

        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1

    t = sorted(dict.values())

    p = t[len(t) - 2]

    print(list(dict.keys())[list(dict.values()).index(p)])