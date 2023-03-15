def dfs(depth,cnt):
    if depth == n-1:
        result.add(cnt+graph[depth])
        result.add(cnt)
        return
    dfs(depth+1,cnt+graph[depth])
    dfs(depth+1,cnt)

for t in range(1,int(input())+1):
    n,b = map(int,input().split())
    graph = list(map(int,input().split()))
    result = set()
    dfs(0,0)
    cnt = 987654321
    for i in list(result):
        if b<=i and cnt>i:
            cnt = i
    print(f"#{t} {cnt-b}")
