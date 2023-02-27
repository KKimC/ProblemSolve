n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]
dp ={}
for i in range(0,100001):
    dp[i*i] = True
result = set()
dx1 = [(i,j) for i in list(range(-9,0))+list(range(9)) for j in list(range(-9,0))+list(range(9))]
dx1.remove((0,0))
for i in range(n):
    for j in range(m):
        for dx,dy in dx1:
            a = ''
            nx = i
            ny = j
            while 0 <= nx < n and 0 <= ny < m:
                a += graph[nx][ny]
                if int(a) in dp:
                    result.add(int(a))
                nx += dx
                ny += dy
if result:
    print(max(result))
else:
    print(-1)
