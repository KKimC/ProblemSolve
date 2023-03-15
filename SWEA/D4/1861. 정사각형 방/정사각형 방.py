dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
def dfs(x,y,xx,yy):
    global flag
    for dx,dy in dx1:
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y]+1:
            dfs(nx,ny,xx,yy)
            result[xx][yy] += 1

for t in range(1,int(input())+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            flag = True
            dfs(i,j,i,j)
    ans =[987654321,0]
    for i in range(n):
        for j in range(n):
            if result[i][j] > ans[1]:
                ans[0] = graph[i][j]
                ans[1] = result[i][j]
            if result[i][j] == ans[1]:
                ans[0] = min(graph[i][j],ans[0])
    print(f"#{t}",ans[0],ans[1]+1)