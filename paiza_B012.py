# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import numpy as np

num = int(input())
cresitID_list = []
for i in range(num):
    cresitID = input().rstrip()
    cresitID_list.append(cresitID)

for i in range(num):
    cresitID = cresitID_list[i]
    gu = np.arange(0, 16, 2)
    ki = np.arange(1, 15, 2)
    even = 0
    for j in gu:
        a = int(cresitID[j]) * 2
        if a >= 10:
            even += int(a / 10) + a % 10
        else:
            even += a
    hoge = 0
    for k in ki:
        hoge += int(cresitID[k])
    total = even + hoge
    shou = int(total / 10)
    shin = (shou + 1) * 10
    sa = shin - total
    if sa != 10:
        answer = sa
    else:
        answer = 0
    print(answer)