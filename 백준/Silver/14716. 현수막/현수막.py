from collections import deque

dx1 = [(-1,0),(0,1),(1,0),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# def dfs(x,y):
#     for dx,dy in dx1:
#         nx = x+dx
#         ny = y+dy
#         if 0<=nx<n and 0<=ny<m and graph[nx][ny]:
#             graph[nx][ny] = 0
#             dfs(nx,ny)

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        xx,yy = q.popleft()
        for dx,dy in dx1:
            nx = xx+dx
            ny = yy+dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]:
                q.append((nx,ny))
                graph[nx][ny] = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            bfs(i,j)
            cnt += 1
print(cnt)