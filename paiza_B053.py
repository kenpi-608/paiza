import numpy as np
H, W = input().rstrip().split(' ')
table = np.zeros((2, int(W)))
row_left = int(H) - 2
col_left = int(W) - 2
for h in range(2):
    retu = input().rstrip().split(' ')
    retu = np.array(retu)
    retu = retu.astype(np.int64)
    sa = retu[1] - retu[0]
    for i in range(int(W) - col_left, int(W)):
        retu = np.append(retu, retu[i - 1] + sa)
    table[h, :] = retu

div = table[1] - table[0]
for j in range(int(H) - row_left, int(H)):
    table = np.vstack([table, table[j - 1] + div])

table = list(table)
for i in range(int(H)):
    for j in range(int(W)):
        if j == int(W) - 1:
            print(int(table[i][j]), end='')
        else:
            print(int(table[i][j]), end=' ')

    print()
 