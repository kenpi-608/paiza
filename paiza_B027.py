# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import numpy as np

H, W, N = input().rstrip().split(' ')
table = [[0 for i in range(int(W))] for j in range(int(H))]
for h in range(int(H)):
    table[h] = list(map(int, input().rstrip().split(' ')))
L = input()
memo = [[0 for i in range(4)] for j in range(int(L))]
for l in range(int(L)):
    memo[l] = list(map(int, input().rstrip().split(' ')))
member = [0 for i in range(int(N))]
turn = 0
l = 0
while l < int(L) - 1:
    while table[memo[l][0] - 1][memo[l][1] - 1] == table[memo[l][2] - 1][memo[l][3] - 1]:
        member[turn] = member[turn] + 2
        if l >= int(L) - 1:
            break
        else:
            l = l + 1 

    if turn < int(N) - 1:
        turn = turn + 1
    else:
        turn = 0
    if l >= int(L) - 1:
        break
    else:
        l = l + 1 

for n in range(int(N)):
    print(member[n])