dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
def dfs(x,y,n,strs):
    if n == 7:
        if len(strs) == 7:
            result.add("".join(strs))
        return
    for dx,dy in dx1:
        nx = x+dx
        ny = y+dy
        if 0<=nx<4 and 0<=ny<4:
            dfs(nx,ny,n+1,strs+graph[nx][ny])

for t in range(1,int(input())+1):
    graph = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,1,graph[i][j])
    print(f"#{t} {len(result)}")