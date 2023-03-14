from collections import defaultdict
from collections import deque

n,m = map(int,input().split())
dic = {}
dicc = {}
graph = defaultdict(list)
result = defaultdict(list)
visited = [0] *(n+1)
visited[1] = 1
flag = False

for i in range(n):
    a = int(input(),2)
    dic[a] = i+1
    dicc[i+1] = a

def bfs(x):
    global flag
    q = deque([dicc[1]])
    while q:
        xx = q.popleft()
        if xx == dicc[x]:
            flag = True
        for i in range(m):
            a = xx^(1 << i)
            if a in dic and not visited[dic[a]]:
                visited[dic[a]] = dic[xx]
                q.append(a)
    return


def back_track(x):
    path = [x]
    while x != 1:
        x = visited[x]
        path.append(x)
    return path


for i in range(int(input())):
    x = int(input())
    bfs(x)
    if visited[x]:
        print(*back_track(x)[::-1])
    else:
        print(-1)