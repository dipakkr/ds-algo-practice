a = [848, 21, 785, 728, 153, 50]


def insertion_sort(a):

    for i in range(6):
        temp = a[i]
        j = i

        while j > 0 and temp < a[j-1]:
            a[j] = a[j-1]
            j = j -1

        a[j] = temp
    print(a)


insertion_sort(a)
