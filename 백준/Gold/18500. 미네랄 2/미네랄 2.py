import sys
from collections import deque

r, c = map(int, input().split())
graph = []
left = []
right = []
dx1 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for i in range(r):
    graph.append(list(input()))
n = int(input())
lst = list(map(int, input().split()))
for i in lst:
    if i % 2:
        right.append(i)
    else:
        left.append(i)
for i in range(r):
    for j in range(c):
        if graph[i][j] == ".":
            graph[i][j] = 0
        else:
            graph[i][j] = 1


def throw_left(l):
    result = 0
    for i in range(c):
        if graph[l][i] != 0:
            graph[l][i] = 0
            return i
    else:
        return -1

def make_one():
    for idx, ial in enumerate(graph):
        for jdx, jal in enumerate(ial):
            if jal:
                graph[idx][jdx] = 1


def throw_right(ri):
    for i in range(c)[::-1]:
        if graph[ri][i] != 0:
            graph[ri][i] = 0
            return i
    else:
        return -1



def find_cluster(x, y, k):
    q = deque([])
    q.append((x, y))
    while q:
        xx, yy = q.popleft()
        graph[xx][yy] = k
        for dx, dy in dx1:
            nx = xx + dx
            ny = yy + dy
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != 0 and graph[nx][ny] != k:
                graph[nx][ny] = k
                q.append((nx, ny))


def find_not_down():
    cluster_set = set()
    for val in graph[r-1]:
        cluster_set.add(val)
    return cluster_set


def down_cluster(k):
    q = deque([])
    for i in range(r)[::-1]:
        for j in range(c)[::-1]:
            if graph[i][j] == k:
                if i+1 != r and (graph[i+1][j] == 0 or graph[i+1][j] == k):
                    q.append((i, j))
                else:
                    return 0
    if not q:return 0
    while q:
        xx, yy = q.popleft()
        graph[xx][yy] = 0
        graph[xx+1][yy] = k
    return 1


for i, val in enumerate(lst):
    if not i % 2:
        l = r - val
        cc = throw_left(l)
        if cc == -1: continue
        if l:
            for idx, (dx, dy) in enumerate(dx1):
                nx = l + dx
                ny = cc + dy
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != 0:
                    find_cluster(nx, ny, idx + 5)
                fset = find_not_down()
                for i in range(5, 9):
                    if i not in fset:
                        while True:
                            if not down_cluster(i):
                                break
        make_one()
    else:
        ri = r - val
        cc = throw_right(ri)
        if cc == -1: continue
        if ri:
            for idx, (dx, dy) in enumerate(dx1):
                nx = ri + dx
                ny = cc + dy
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != 0:
                    find_cluster(nx, ny, idx + 5)
            fset = find_not_down()
            for i in range(5, 9):
                if i not in fset:
                    while True:
                        if not down_cluster(i):
                            break
        make_one()

for idx, ial in enumerate(graph):
    for jdx, jal in enumerate(ial):
        if jal:
            graph[idx][jdx] = "x"
        else:
            graph[idx][jdx] = "."

for i in graph:
    print(*i,sep="")

# for i in graph:
#     if not i%2:
#         l = r - left[i//2]
#         cc = throw_left(l)
#         if l:
#             find_cluster(l - 1, cc, 3)
#             down_cluster(3)
#     else:
#         ri = c - right[i//2+1]
#         cc = throw_right(ri)
#         if ri:
#             find_cluster(ri, cc, 4)
#             down_cluster(4)