from collections import deque
a,m = map(int,input().split())
visited = [0]*100001
def bfs(x):
    q = deque([x])
    while q:
        n = q.popleft()
        if n == m:
            break
        if 0<n*2 <= 100000 and not visited[n*2]:
            q.append(n*2)
            visited[n*2] = visited[n]+1
        if n+1 <= 100000 and not visited[n+1]:
            q.append(n+1)
            visited[n+1] = visited[n]+1
        if 0<=n-1 <= 100000 and not visited[n-1]:
            q.append(n-1)
            visited[n-1] = visited[n]+1
        
bfs(a)
print(visited[m])