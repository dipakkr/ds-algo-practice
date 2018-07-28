
a = "aaaaaaaabbbccccddddd"

a_len = len(a)

count = 1

for i in range(a_len):

    cr_count = 1
    for j in range(i+1, a_len):

        if a[i] != a[j]:
            break
        cr_count += 1

    if cr_count > count:
        count = cr_count

print(count)