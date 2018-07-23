
a = []
matrix1 = []

# Input Matrix 1
for i in range(3):
    a = []
    for j in range(3):
        a.append(input())
    matrix1.append(a)

print(matrix1)


# Input Matrix 2

a = []
matrix2 = []

for i in range(3):
    a = []
    for j in range(3):
        a.append(input())
    matrix2.append(a)

print(matrix2)

# Multiplication
result = []

# rows of X
for i in range(len(matrix1)):

    # Columns Of Y
    for j in range(len(matrix2[0])):
        # Rows of Y
        for k in range(len(matrix2)):
            result.append(result[i][j] + (matrix1[i][k] * matrix2[k][j]))


print(matrix2)

