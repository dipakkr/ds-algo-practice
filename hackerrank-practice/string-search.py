
strings = ['aba', 'baba', 'aba', 'xzxb']

queries = ['aba', 'xzxb', 'ab']


def sparse_array(s, q):

    len_s = len(s)
    len_q = len(q)

    for i in range(len_q):
        count = 0
        for j in range(len_s):
            if s[j] == q[i]:
                count += 1
                print(s[j])
        print(count)


sparse_array(strings, queries)
