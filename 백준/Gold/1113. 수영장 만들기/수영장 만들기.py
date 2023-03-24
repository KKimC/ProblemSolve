
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,list(input()))) for _ in range(n)]
dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
new_graph = [i[::] for i in graph]
def bfs(x,y):
    global cnt
    q = deque([(x,y)])
    h = []
    qq = deque([(x,y)])
    while q:
        xx,yy = q.popleft()
        for dx,dy in dx1:
            nx = xx+dx
            ny = yy+dy
            if 0>nx or n<=nx or ny<0 or m<=ny:
                return 0,0
            if visited[nx][ny]:continue
            if graph[nx][ny] > graph[x][y]:
                h.append(graph[nx][ny])
            else:
                visited[nx][ny] = True
                q.append((nx,ny))
                qq.append((nx,ny))
    minn = min(h)
    while qq:
        xx,yy = qq.popleft()
        if minn > new_graph[xx][yy]:
            cnt += minn - new_graph[xx][yy]
            new_graph[xx][yy] = minn
    return
dic = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
visited = [[False]*m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        for ii in range(n):
            for jj in range(m):
                visited[ii][jj] = False
        visited[ii][jj] = True
        bfs(i,j)
print(cnt)