
# You are given a list of n-1 integers and these integers are in the range of 1 to n.
# There are no duplicates in list. One of the integers is missing in the list.
# Write an efficient code to find the missing integer.


n = 10
a = [1, 2, 3, 8,  7, 9]
b = [0]*n

# Approach 1 - If only 1 number is missing

s = n*(n-1) / 2
sum_list = sum(a)
missing_no = s - sum_list
print(int(missing_no))

# Approach 2 - In case multiple missing
for i in range(len(a)):
    temp = a[i]
    if b[temp] == 0:
        b[temp] = 1

for i in range(1, len(b)):
    if b[i] == 0:
        print(i),
