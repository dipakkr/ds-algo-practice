
# element is leader if all the elment to right side is smaller


t = int(input())

for _ in range(t):

    n = int(input())
    x = list(map(int, input().strip(' ').split()))

    # element is leader if all the elment to right side is smaller
    c = []
    if len(x) > 1:
        for i in range(len(x)):

            a1 = x[i]
            a2 = x[i + 1:]

            if a2:
                m = max(a2)
            if a1 > m:
                c.append(a1)

        c.append(x[len(x) - 1])
    else:
        c.append(x[len(x) - 1])

    for i in range(len(c)):
        print(c[i], end=' ')

    print()

