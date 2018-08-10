t = int(input())

while t > 0:

    v = ['a', 'e', 'i', 'o', 'u']
    s = input()
    v_count = 0
    c_count = 0

    for i in s:

        if i in v:
            print("in vowel")
            v_count += 1
            c_count = 0
        elif i == '?':
            print("in ? ")
            v_count += 1
            c_count += 1
        else:
            print("in consonant")
            c_count += 1
            v_count = 0

    if v_count > 5 or c_count > 3:
        print("in eval")
        print(0)
    else:
        print("in eval")
        print(1)

    t -= 1