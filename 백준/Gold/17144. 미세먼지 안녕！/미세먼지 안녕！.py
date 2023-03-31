n,m,t = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cleaner = []
dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
for i in range(n):
    if graph[i][0] == -1:
        cleaner.append(i)

for _ in range(t):
    cnt = []
    for i in range(n):
        for j in range(m):
            if graph[i][j]>4:
                a = graph[i][j] // 5
                for dx,dy in dx1:
                    nx = i+dx
                    ny = j+dy
                    if 0<=nx<n and 0<=ny<m and graph[nx][ny] != -1:
                        cnt.append((nx,ny,a))
                        graph[i][j] -= a
    for x,y,num in cnt:
        graph[x][y] += num

    graph[cleaner[0]-1][0] = 0
    for i in range(cleaner[0]-1)[::-1]:
        if graph[i][0]:
            graph[i+1][0] = graph[i][0]
            graph[i][0] = 0
    for i in range(1,m):
        if graph[0][i]:
            graph[0][i-1] = graph[0][i]
            graph[0][i] = 0
    for i in range(1,cleaner[0]+1):
        if graph[i][m-1]:
            graph[i-1][m-1] = graph[i][m-1]
            graph[i][m-1] = 0
    for i in range(1,m-1)[::-1]:
        if graph[cleaner[0]][i]:
            graph[cleaner[0]][i+1] = graph[cleaner[0]][i]
            graph[cleaner[0]][i] = 0

    graph[cleaner[1]+1][0] = 0
    for i in range(cleaner[1]+2,n):
        if graph[i][0]:
            graph[i-1][0] = graph[i][0]
            graph[i][0] = 0
    for i in range(1,m):
        if graph[n-1][i]:
            graph[n-1][i-1] = graph[n-1][i]
            graph[n-1][i] = 0
    for i in range(cleaner[1],n-1)[::-1]:
        if graph[i][m-1]:
            graph[i+1][m-1] = graph[i][m-1]
            graph[i][m-1] = 0
    for i in range(1,m-1)[::-1]:
        if graph[cleaner[1]][i]:
            graph[cleaner[1]][i+1] = graph[cleaner[1]][i]
            graph[cleaner[1]][i] = 0
result = 0
for i in graph:
    for j in i:
        if j>0:
            result += j
print(result)