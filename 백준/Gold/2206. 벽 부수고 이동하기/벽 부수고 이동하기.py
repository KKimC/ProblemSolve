from collections import deque
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,list(input()))))
visited = [[0] * m for i in range(n)]
visited2 = [[0] * m for i in range(n)]
dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
def find_graph():
    for i in graph:
        for j in i:
            if j != 0:
                return True
    else:
        return False
def bfs(x,y):
    q = deque([(x,y,False)])
    while q:
        xx,yy,flag = q.popleft()
        for dx,dy in dx1:
            nx = xx+dx
            ny = yy+dy
            if 0<=nx<n and 0<=ny<m and not graph[nx][ny]:
                if not flag and not visited[nx][ny]:
                    visited[nx][ny] = visited[xx][yy]+1
                    q.append((nx,ny,False))
                elif flag and not visited2[nx][ny]:
                    visited2[nx][ny] = visited2[xx][yy] + 1
                    q.append((nx, ny, True))
            elif 0<=nx<n and 0<=ny<m and graph[nx][ny] and not flag:
                visited2[nx][ny] = visited[xx][yy]+1
                q.append((nx,ny,True))
bfs(0,0)
if find_graph() and visited[n-1][m-1] and visited2[n-1][m-1]:
    print(min(visited[n-1][m-1], visited2[n-1][m-1])+1)
elif visited[n-1][m-1]:
    print(visited[n-1][m-1]+1)
elif visited2[n-1][m-1]:
    print(visited2[n-1][m-1]+1)
elif not find_graph():
    print(n+m-1)
else:
    print(-1)