import sys
from collections import deque
n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
graph = [[5] * n for _ in range(n)]
tree = deque([])
for _ in range(m):
    x, y, age = map(int, sys.stdin.readline().rstrip().split())
    tree.append((age, x - 1, y - 1))

q = deque([])
dx1 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for _ in range(k):
    new_tree = deque([])
    while tree:
        age, x, y = tree.popleft()
        if graph[x][y] >= age:
            graph[x][y] -= age
            if age%5 == 4:
                for dx, dy in dx1:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        new_tree.appendleft((1, nx, ny))
            new_tree.append((age+1, x, y))
            continue
        q.append((age // 2, x, y))
    tree = new_tree
    while q:
        age, x, y = q.pop()
        graph[x][y] += age
    for i in range(n):
        for j in range(n):
            graph[i][j] += A[i][j]

print(len(tree))