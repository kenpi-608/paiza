import numpy as np

def isPheromone(ant_map, y, x):
    if ant_map[y, x] != '#':
        return False
    else:
        return True

"""
深さ優先探索
"""
def isreachable(ant_map, search_map, feed_y, feed_x, H, W):
    # print("(y, x)= (%d, %d)" % (feed_y, feed_x))
    # print(search_map)
    if (feed_y == 0) and (feed_x == 0):
        return True
    search_map[feed_y, feed_x] = True
    for (next_y, next_x) in [(feed_y - 1, feed_x), (feed_y, feed_x - 1), (feed_y + 1, feed_x), (feed_y, feed_x + 1)]:
        if (next_y < 0) or (next_x < 0):
            continue
        if (next_y > H) or (next_x > W):
            continue
        if (search_map[next_y, next_x] == True):
            continue
        if isPheromone(ant_map, next_y, next_x):
            if(isreachable(ant_map, search_map, next_y, next_x, H, W)):
                return True
            else:
                continue
    return False

if __name__ == '__main__':
    H, W = input().rstrip().split(' ')
    ant_map = []
    for i in range(int(H)):
        ant_map.append(list(input().rstrip()))
    ant_map = np.array(ant_map)
    N = int(input())

    feed_list = [list(map(int,input().split())) for i in range(N)]
    cannot = False
    for i in range(N):
        # print(i)
        if ant_map[feed_list[i][0] - 1, feed_list[i][1] - 1] != '#':
            cannot = True
            print('NO')
            break
        search_map = np.array([[False for i in range(ant_map.shape[1])] for j in range(ant_map.shape[0])])
        if isreachable(ant_map, search_map, feed_list[i][0] - 1, feed_list[i][1] - 1, int(H) - 1, int(W) - 1) == False:
            cannot = True
            print('NO')
            break

    if cannot == False:
        print('YES')


