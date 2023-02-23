from collections import deque
dx1 = [(-1,0),(1,0),(0,1),(0,-1)]
def bfs(x,y,s):
    q = deque([(x,y)])
    visited[x][y] = True
    while q:
        xx,yy = q.popleft()
        for dx,dy in dx1:
            nx = xx+dx
            ny = yy+dy
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == s and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,graph[i][j])
            count += 1
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"
count1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,graph[i][j])
            count1 += 1
print(count,count1)