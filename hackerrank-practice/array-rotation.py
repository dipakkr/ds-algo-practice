
def left_rotation(a, n):

    for i in range(n):
        x = len(a)
        temp = a[0]
        for i in range(x-1):
            if i != x-1:
                a[i] = a[i+1]
                print(a[i])
            else:
                a[i] = a[x-1]
        a[i+1] = temp
        print("after loop 1 ==> ")
        print(a)


if __name__ == '__main__':
    x = input('Type Here : ')
    x_list = list(x)
    left_rotation(x_list, 2)