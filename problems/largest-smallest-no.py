a = [3, 4, 1, 2, 10, 20]

# smallest and largest  in unsorted array

temp = a[0]
s_temp = a[0]
for i in range(len(a)):
    # For largest no.
    if temp < a[i]:
        temp = a[i]

    # For smallest no
    if s_temp > a[i]:
        s_temp = a[i]

print("smallest --> " + str(s_temp))
print("largest ---> " + str(temp))
