# code

n = int(input())
x = list(map(int, input().strip(' ').split()))
q = int(input())

for i in range(q):

    q1 = list(map(int, input().strip(' ').split()))

    l = q1[0]
    r = q1[1]

    y = []

    for i in range(l, r + 1):
        y.append(x[i])

    y = sorted(y)

    if len(y) > 1:
        if y[1] > y[0]:
            print(y[1])
        else:
            print("-1")
