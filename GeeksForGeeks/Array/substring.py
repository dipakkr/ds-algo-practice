
def divideString(input1, input2, input3):

    l = len(input)
    r = l % 3
    div = l / 3
    print(div)

    chunk_size = int(div)

    x= []
    if r == 0:
        for i in range(0, l, chunk_size):
            x.append(input[i:i+chunk_size])

    print(x)


divideString('john', 'johny', 'janardhan')