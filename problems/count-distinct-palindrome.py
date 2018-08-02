n = int(input())

while n > 0:
    s1 = input()
    x = list(s1)
    len_x1 = len(x)
    count = len(set(x))

    # palindrome algorithm

    t = []

    for i in range(len_x1):
        p  = x[i]
        for j in range(i+1, len_x1):
            p = p + x[j]
            p1 = p[::-1]
            if p == p1:
                t.append(p1)

    count = count + len(set(t))
    print(count)

    n -= 1