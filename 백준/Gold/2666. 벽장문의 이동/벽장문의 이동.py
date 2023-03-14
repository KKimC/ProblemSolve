n = int(input())
a,b = map(int,input().split())
graph = []
for _ in range(int(input())):
    graph.append(int(input()))
nn = len(graph)
minn = 987654321
def dfs(x,aa,bb,summ):
    global minn
    if summ > minn:
        return
    if x == nn:
        if summ < minn:
            minn = summ
        return
    ii = graph[x]
    if aa <= ii <= bb:
        dfs(x+1,ii,bb,summ+abs(ii-aa))
        dfs(x+1,aa,ii,summ+abs(ii-bb))
    else:
        if abs(ii-aa) < abs(ii-bb):
            dfs(x+1,ii,bb,summ+abs(ii-aa))
        else:
            dfs(x+1,aa,ii,summ+abs(ii-bb))
dfs(0,a,b,0)
print(minn)