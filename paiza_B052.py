# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

import numpy as np

def location_selector(x, y, field, H, W):
    location_num = field[y][x]
    kita = float("inf")
    higashi = float("inf")
    minami = float("inf")
    nishi = float("inf")
    for i in range(max(max(field))):
        if y >= 1:
            kita = field[y - 1][x]
        if x < int(W) - 1:
            higashi = field[y][x + 1]
        if y < int(H) - 1:
            minami = field[y + 1][x]
        if x >= 1:
            nishi = field[y][x - 1]
        if kita < location_num:
            y = y - 1
        elif higashi < location_num:
            x = x + 1
        elif minami < location_num:
            y = y + 1
        elif nishi < location_num:
            x = x - 1     
        else:
            break
    return x, y

H, W, N = input().rstrip().split(' ')
particle = []
field = [[0 for i in range(int(W))] for j in range(int(H))]
for i in range(int(N)):
    x, y = input().rstrip().split(' ')
    particle.append([int(x), int(y)])
for i in range(int(N)):
    x = particle[i][0] - 1
    y = particle[i][1] - 1
    x, y = location_selector(x, y, field, H, W)
    field[y][x] = field[y][x] + 1
    
for i in range(int(H)):
    for j in range(int(W)):
        if j != int(W) - 1:
            print(field[i][j], end=" ")
        else: 
            print(field[i][j])
    # print()
    