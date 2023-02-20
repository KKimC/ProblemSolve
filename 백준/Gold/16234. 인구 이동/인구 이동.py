from collections import deque
dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
def bfs(x,y):
    visited[x][y] = True
    q = deque([(x,y)])
    xyq = deque([(x,y)])
    while q:
        xx,yy = q.popleft()
        for dx,dy in dx1:
            nx = xx+dx
            ny = yy+dy
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and l <= abs(graph[xx][yy] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    xyq.append((nx,ny))
    return xyq

def arr_copy(arr):
    arr2 = []
    for i in arr:
        arr2.append(i[:])
    return arr2


n,l,r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
while True:
    result = arr_copy(graph)
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                count = 0
                xyq = bfs(i,j)
                for x,y in xyq:
                    count += graph[x][y]
                for x,y in xyq:
                    if not graph[x][y] == count//len(xyq):
                        graph[x][y] = count//len(xyq)
    c = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == result[i][j]:
                c += 1
    if c == n*n:break
    cnt += 1
print(cnt)
