a = 2
b = 3


def gcd(a, b):

    if a == b:
        x = a
    elif a > b:
        x = gcd(a-b, b)
    else:
        x = gcd(a, b-a)

    return x


def lcm(a, b):

    return (a*b) /  gcd(a, b)


print('LCM of ', a, 'and ', b, 'is', lcm(a, b))