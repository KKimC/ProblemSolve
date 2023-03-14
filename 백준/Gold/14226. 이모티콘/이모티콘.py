from collections import deque
s = int(input())
visited = [[False]*(s+1) for _ in range(s+1)]


def bfs():
    q = deque([(1, 0)])
    while q:
        x, cb = q.popleft()
        if x == s:
            print(visited[x][cb])
            return
        if x > 1 and not visited[x-1][cb]:
            visited[x - 1][cb] = True
            visited[x-1][cb] = visited[x][cb] + 1
            q.append((x-1, cb))
        if not visited[x][x]:
            visited[x][x] = True
            visited[x][x] = visited[x][cb] + 1
            q.append((x, x))
        if x+cb<s+1 and not visited[x+cb][cb]:
            visited[x + cb][cb] = True
            visited[x+cb][cb] = visited[x][cb]+1
            q.append((x+cb, cb))

bfs()