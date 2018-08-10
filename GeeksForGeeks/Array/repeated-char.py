t = int(input())

for j in range(t):

    s = input()
    dict = {}

    for i in s:

        keys = dict.keys()

        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in s:

        if dict[i] > 1:
            x = i
            print(x)
            break
        else:
            x = -1
            print(x)

    print(x)