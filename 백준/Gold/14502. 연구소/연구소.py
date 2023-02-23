from collections import deque
from copy import deepcopy
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx1 = [(-1,0),(1,0),(0,1),(0,-1)]
visited = [[True]*m for _ in range(n)]
def bfs(x,y):
    q = deque([(x,y)])
    while q:
        xx,yy = q.popleft()
        for dx,dy in dx1:
            nx = xx+dx
            ny = yy+dy
            if 0<=nx<n and 0<=ny<m and not graph2[nx][ny]:
                graph2[nx][ny] = 2
                q.append((nx,ny))

def dfs(n,arr):
    if n == 3:
        result.append(arr)
        return
    for i in range(len(virus)):
        if not visited[i]:
            visited[i] = True
            arr2 = arr[:]
            arr2.append(virus[i])
            dfs(n+1,arr2)
            visited[i] = False
result = []
virus = []
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            virus.append((i,j))
visited = [False]*len(virus)
dfs(0,[])
minn = 0
for i in result:
    for x,y in i:
        graph[x][y] = 1
    graph2 = deepcopy(graph)
    q1 = deque([])
    for idx, ial in enumerate(graph2):
        for jdx, jal in enumerate(ial):
            if jal == 2:
                q1.append((idx,jdx))
    while q1:
        x,y = q1.popleft()
        bfs(x,y)
    count = 0
    for ii in graph2:
        for j in ii:
            if j == 0:
                count += 1
    minn = max(count,minn)
    for x,y in i:
        graph[x][y] = 0
print(minn)