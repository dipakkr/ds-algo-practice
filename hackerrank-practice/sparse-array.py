

strings = ['abba', 'baba', 'aba', 'xzxb']

queries = ['aba', 'xzxb', 'ab']


def sparse_array(s, q):

    len_s = len(s)

    b = []

    len_q = len(q)

    for i in range(len_s):
        y = len(strings[i])
        sub_list_s = list(s[i])
        for j in range(y):
            if j == 0:
                xx = sub_list_s[0]
                r = xx
                b.append(r)
            else:
                r = r + sub_list_s[j]
                b.append(r)
    print(b)

    len_b = len(b)

    count = 0

    for i in range(len_q):
        for j in range(len_b):
            if b[j] == q[i]:
                count += 1
                print(b[j])
        print(count)

            
sparse_array(strings, queries)
