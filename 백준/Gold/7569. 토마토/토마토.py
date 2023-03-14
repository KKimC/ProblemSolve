import sys
from collections import deque

input = sys.stdin.readline

# dx -> n, dy -> m, dh -> h
dx, dy, dh = [0, 0, 1, -1], [1, -1, 0, 0], [1, -1]
ripen = []
graph = []
m, n, h = map(int, input().rstrip().split())

visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

tomato_check = False


# 3차원 배열에 채워 넣음
for i in range(h):
    temp = []
    for j in range(n):
        a = list(map(int, input().rstrip().split()))
        temp.append(a)
        for k in range(m):
            if a[k] == 1:
                ripen.append((i, j, k))

    graph.append(temp)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                tomato_check = True


if not tomato_check:
    print(0)
    exit(0)

max_value = -1e9


def dfs():
    global max_value
    q = deque(ripen)

    while q:
        z, x, y = q.popleft()
        visited[z][x][y] = 1

        # 같은 차원 토마토부터 순회
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[z][nx][ny] and not graph[z][nx][ny]:
                    graph[z][nx][ny] = graph[z][x][y] + 1
                    max_value = max(max_value, graph[z][x][y])
                    q.append((z, nx, ny))

        # 위, 아래 토마토 순회
        for i in range(2):
            nh = z + dh[i]

            if 0 <= nh < h:
                if not visited[nh][x][y] and not graph[nh][x][y]:
                    graph[nh][x][y] = graph[z][x][y] + 1
                    max_value = max(max_value, graph[z][x][y])
                    q.append((nh, x, y))


zero_check = False

dfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                zero_check = True

if zero_check:
    print(-1)
else:
    print(max_value)