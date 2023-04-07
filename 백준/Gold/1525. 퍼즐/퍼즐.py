from collections import deque

dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
result = 0
graph = [input().split() for _ in range(3)]
visit_str = ''.join(j.strip() for i in graph for j in i)
visited = {visit_str}
target = '123456780'
result = 987654321
flag = False
x,y = 0,0

for i in range(3):
    for j in range(3):
        if graph[i][j] == '0':
            x = i
            y = j

def bfs(xx,yy,v):
    global result, flag
    q = deque([(xx,yy,0,v)])
    while q:
        x,y,depth,visit_str2 = q.popleft()
        graph[0][0] = visit_str2[0]
        graph[0][1] = visit_str2[1]
        graph[0][2] = visit_str2[2]
        graph[1][0] = visit_str2[3]
        graph[1][1] = visit_str2[4]
        graph[1][2] = visit_str2[5]
        graph[2][0] = visit_str2[6]
        graph[2][1] = visit_str2[7]
        graph[2][2] = visit_str2[8]
        if visit_str2 == target:
            result = min(result, depth)
            flag = True
            return
        for dx,dy in dx1:
            nx = x+dx
            ny = y+dy
            if 0<=nx<3 and 0<=ny<3:
                graph[x][y] = graph[nx][ny]
                graph[nx][ny] = '0'
                visit_str = ''.join(j.strip() for i in graph for j in i)
                if visit_str not in visited:
                    visited.add(visit_str)
                    q.append((nx,ny,depth+1,visit_str))
                graph[nx][ny] = graph[x][y]
                graph[x][y] = '0'

bfs(x,y,visit_str)
if flag:
    print(result)
else:
    print(-1)