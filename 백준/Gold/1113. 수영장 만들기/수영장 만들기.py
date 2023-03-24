from collections import deque

def bfs(x, y, height):
    q = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1
    flag = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if (not visited[nx][ny]) and (graph[nx][ny] <= height):
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
            else:
                flag = True

    return cnt if not flag else 0

n,m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
ans = 0
for height in range(1, 9):
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (not visited[i][j]) and (graph[i][j] <= height):
                ans += bfs(i, j, height)

print(ans)