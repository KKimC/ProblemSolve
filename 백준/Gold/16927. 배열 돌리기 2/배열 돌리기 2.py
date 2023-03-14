from collections import deque
n,m,r = map(int,input().split())
shell = min(n,m)//2
q = deque()
graph = [list(map(int,input().split())) for _ in range(n)]
for i in range(shell):
    q.extend(graph[i][i:m-i])
    q.extend([graph2[m-i-1] for graph2 in graph[i+1:n-i-1]])
    q.extend(graph[n-1-i][i:m-i][::-1])
    q.extend([graph2[i] for graph2 in graph[i+1:n-i-1]][::-1])
    for _ in range(r%len(q)):
        q.append(q.popleft())
    for idx in range(i,m-i):
        graph[i][idx] = q.popleft()
    for idx in range(i+1,n-i-1):
        graph[idx][m-i-1] = q.popleft()
    for idx in range(m-i-1,i-1,-1):
        graph[n-i-1][idx] = q.popleft()
    for idx in range(n-i-2, i, -1):
        graph[idx][i] = q.popleft()
for i in graph:
    print(*i)