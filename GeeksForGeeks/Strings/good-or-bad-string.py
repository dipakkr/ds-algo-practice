def isBad(s):
    cons = 0
    vowel = 0
    v = ['a','e','i','o','u']

    for i in s:
        if i in v:
            print("in vowel")
            vowel += 1
            cons = 0
        elif i == '?':
            print("in ?")
            cons += 1
            vowel += 1
        else:
            print("in conso")
            cons += 1
            vowel = 0

        if cons > 3 or vowel > 5:
            print("in eval")
            print(0)
            return
    print(1)


t = int(input())
for i in range(t):
    isBad(input())