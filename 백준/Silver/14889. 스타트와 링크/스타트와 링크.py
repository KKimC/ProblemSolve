n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
result = 987654321

def dfs(depth,A):
    global result
    if len(A) == n//2:
        a_cnt = 0
        b_cnt = 0
        for i in range(n):
            for j in range(i,n):
                if i in A and j in A:
                    a_cnt += graph[i][j]
                    a_cnt += graph[j][i]
                if i not in A and j not in A:
                    b_cnt += graph[i][j]
                    b_cnt += graph[j][i]
        result = min(result,abs(a_cnt-b_cnt))
        return
    if len(A)>n//2:
        return
    if depth == n:
        return
    dfs(depth+1,A+[depth])
    dfs(depth+1,A)

dfs(0,[])
print(result)

