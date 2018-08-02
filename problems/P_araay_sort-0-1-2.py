
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip(' ').split(' ')))
    a = sorted(a)
    for i in range(n):
        print(a[i], end=' ')
    print()
