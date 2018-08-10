# def fib(n):
#     if n == 1 or n == 2: return 1;
#
#     return fib(n - 2) + fib(n - 1)
#


# Using Array memorization

def fib(n):

    x = [1, 1]

    for i in range(n):
        sum = x[len(x)-1] + x[len(x) - 2]
        x.append(sum)

    print(x[n-1])


print(fib(40))
