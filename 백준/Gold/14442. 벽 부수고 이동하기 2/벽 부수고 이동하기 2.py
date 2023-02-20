from collections import deque
n,m,k = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,list(input()))))
visited = [[[0] * m for _ in range(n)] for _ in range(11)]
dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
def find_graph():
    for i in graph:
        for j in i:
            if j != 0:
                return True
    else:
        return False
def bfs(x,y):
    q = deque([(x,y,0)])
    while q:
        xx,yy,count = q.popleft()
        for dx,dy in dx1:
            nx = xx+dx
            ny = yy+dy
            if not (0 <= nx < n) or not (0 <= ny < m):continue
            if not graph[nx][ny]:
                if count <= k and not visited[count][nx][ny]:
                    visited[count][nx][ny] = visited[count][xx][yy]+1
                    q.append((nx,ny,count))
            else:
                if count < k and not visited[count+1][nx][ny]:
                    visited[count+1][nx][ny] = visited[count][xx][yy]+1
                    q.append((nx,ny,count+1))
bfs(0,0)
result = []
for i in range(11):
    if visited[i][n-1][m-1]:
        result.append(visited[i][n-1][m-1])
if find_graph():
    if result:
        print(min(result)+1)
    else:
        print(-1)
else:
    print(n+m-1)