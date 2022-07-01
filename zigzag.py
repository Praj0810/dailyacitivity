def zigzag(s, numRows):

    if numRows == 1 or numRows >= len(s):
        return s

    res = [''] * numRows
    index = 0
    increment = 1

    for char in s:
        res[index] += char
        if index == 0:
            increment = 1
        elif index == numRows -1:
            increment = -1
        index += increment
        print(res)

    return ''.join(res)

s = "PAYPALISHIRING"
#s  = "P"
#numRows = 1
#numRows = 4
numRows = 3

print(zigzag(s, numRows))


