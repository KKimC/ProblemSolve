n = int(input())
stats = [list(map(int, input().split())) for i in range(n)]
visited = [0] * n
ans = 987654321


def dfs(x):
    global ans
    if x == n:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += stats[i][j]
                elif not visited[i] and not visited[j]:
                    link += stats[i][j]
        ans = min(ans, abs(start - link))
        return
    visited[x] = 1
    dfs(x + 1)
    visited[x] = 0
    dfs(x + 1)
dfs(0)

print(ans)