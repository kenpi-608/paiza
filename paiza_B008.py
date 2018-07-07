# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import numpy as np
N, M = input().rstrip().split(' ')
table = np.zeros((int(N), int(M)))
for m in range(int(M)):
    vec = input().rstrip().split(' ')
    vec = np.array(vec)
    vec = vec.astype(np.int64)
    table[:, m] = vec
soneki = table.sum(axis=0)
answer = 0
if soneki[soneki > 0].shape[0] == 0:
    answer = 0
else:
    answer = soneki[soneki > 0].sum()
print(int(answer))