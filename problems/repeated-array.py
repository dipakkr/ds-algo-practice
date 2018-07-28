
# find the repeated number in the array


def printrepeating(arr, size):

    for i in range(0, size):
        print(arr)
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]

        else:
            print(abs(arr[i]), end=" ")


a = [1, 2, 3, 1, 3, 6, 6]
a_size = len(a)

printrepeating(a, a_size)