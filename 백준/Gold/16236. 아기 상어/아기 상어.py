from collections import deque

def printt():
    for i in graph:
        print(*i)

def check_time(x, y, dx, dy):
    return abs(x-dx) + abs(y-dy)


def eat_fish():
    global shark
    shark[1] += 1
    if shark[0] == shark[1]:
        shark[0] += 1
        shark[1] = 0


def bfs(x,y,t):
    global shark
    lst = []
    q = deque([])
    q.append((x,y,t))
    graph[x][y] = 0
    visited[x][y] = True
    while q:
        xx, yy, t = q.popleft()

        for dx, dy in dx1:
            nx = xx+dx
            ny = yy+dy
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] <= shark[0] and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx,ny,t+1))
                if graph[nx][ny] != 0 and graph[nx][ny] < shark[0]:
                    lst.append([nx,ny,t+1])
    if lst:

        lst.sort(key = lambda i :(i[2],i[0],i[1]))
        # print(x,y)
        # print(lst)
        fx, fy, t = lst[0]
        graph[fx][fy] = 9
        eat_fish()
        # print("shark = ", shark)
        # print("t = ", check_time(x,y,fx,fy))
        # printt()
        return fx,fy,t
    return 0, 0, -1


n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
shark = [2,0]
dx1 = [(-1,0),(0,-1),(0,1),(1,0)]
visited = [[False] * n for _ in range(n)]
for idx, ial in enumerate(graph):
    for jdx, jal in enumerate(ial):
        if jal == 9:
            mx = idx
            my = jdx
count = 0
while True:
    mx, my, t = bfs(mx,my,0)

    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    if t == -1:
        break
    else:
        count += t
print(count)
