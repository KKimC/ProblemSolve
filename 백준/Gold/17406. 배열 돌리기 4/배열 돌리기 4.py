from collections import deque


def turn(r,c,s):
    x = r-s-1
    y = c-s-1
    xx = r+s
    yy = c+s
    shell = s
    for i in range(s):
        q.extend(graph[x+i][y+i:yy-i])
        q.extend([graph2[yy-i-1] for graph2 in graph[x+i+1:xx-i-1]])
        q.extend(graph[xx-1-i][y+i:yy-i][::-1])
        q.extend([graph2[y+i] for graph2 in graph[x+i+1:xx-i-1]][::-1])
        q.appendleft(q.pop())
        for idx in range(y+i,yy-i):
            graph[x+i][idx] = q.popleft()
        for idx in range(x+i+1,xx-i-1):
            graph[idx][yy-i-1] = q.popleft()
        for idx in range(yy-i-1,y+i-1,-1):
            graph[xx-i-1][idx] = q.popleft()
        for idx in range(xx-i-2, x+i, -1):
            graph[idx][y+i] = q.popleft()

def turn_back(r,c,s):
    x = r-s-1
    y = c-s-1
    xx = r+s
    yy = c+s
    for i in range(s):
        q.extend(graph[x+i][y+i:yy-i])
        q.extend([graph2[yy-i-1] for graph2 in graph[x+i+1:xx-i-1]])
        q.extend(graph[xx-1-i][y+i:yy-i][::-1])
        q.extend([graph2[y+i] for graph2 in graph[x+i+1:xx-i-1]][::-1])
        q.append(q.popleft())
        for idx in range(y+i,yy-i):
            graph[x+i][idx] = q.popleft()
        for idx in range(x+i+1,xx-i-1):
            graph[idx][yy-i-1] = q.popleft()
        for idx in range(yy-i-1,y+i-1,-1):
            graph[xx-i-1][idx] = q.popleft()
        for idx in range(xx-i-2, x+i, -1):
            graph[idx][y+i] = q.popleft()

def dfs(c):
    global result
    if c == k:
        for i in graph:
            cnt = 0
            for j in i:
                cnt += j
            if cnt < result:
                result = cnt
        return
    for i in range(k):
        if not visited[i]:
            visited[i] = True
            turn(*turns[i])
            dfs(c+1)
            visited[i] = False
            turn_back(*turns[i])


n,m,k = map(int,input().split())

q = deque()
graph = [list(map(int,input().split())) for _ in range(n)]
turns = []
for _ in range(k):
    r,c,s = map(int,input().split())
    turns.append((r,c,s))
result = 10001
visited = [False]*k
dfs(0)
print(result)