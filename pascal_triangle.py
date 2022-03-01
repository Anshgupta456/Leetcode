numrows = 6
res = [[1]]
for i in range(numrows-1):
    ary = [0] + res[-1] + [0]
    row = []
    for j in range(len(res[-1])+1):
        row.append(ary[j] + ary[j + 1])
    res.append(row)
print(res)