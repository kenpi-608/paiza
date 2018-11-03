T, x, y = input().rstrip().split(' ')
T = int(T)
x = int(x)
y = int(y)
xmax = x
for t in range(T):
    a, b = input().rstrip().split(' ')
    a = int(a)
    b = int(b)
    y = y + b
    if y <= 0:
        break
    else:
        x = x + a
        if xmax < x:
            xmax = x
print(xmax)
