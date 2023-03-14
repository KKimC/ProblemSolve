from collections import deque

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(input())
dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
def bfs(x,y):
    q = deque([(x,y,0)])
    while q:
        xx,yy,cnt = q.popleft()
        for dx,dy in dx1:
            nx = xx+dx
            ny = yy+dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == "L" and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny,cnt+1))
    return cnt

result = []
for idx, ial in enumerate(graph):
    for jdx, jal in enumerate(ial):
        visited = [[False] * m for _ in range(n)]
        if jal == "L":
            visited[idx][jdx] = True
            result.append(bfs(idx,jdx))

print(max(result))