import sys

sys.setrecursionlimit(10000)
dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
def dfs(x,y):
    for dx,dy in dx1:
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]:
                graph[nx][ny] = 0
                dfs(nx,ny)

for _ in range(int(input())):
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                graph[i][j] = 0
                dfs(i,j)
                count += 1
    print(count)