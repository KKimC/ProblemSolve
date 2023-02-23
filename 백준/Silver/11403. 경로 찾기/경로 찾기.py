from collections import deque
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
result = [[0]*n for _ in range(n)]
q = deque([])
for idx, ial in enumerate(graph):
    for jdx, jal in enumerate(ial):
        if jal:
           q.append((idx,jdx))
q.extend(q)
q.extend(q)
q.extend(q)
q.extend(q)

while q:
    x,y = q.popleft()
    result[x][y] = 1
    for i in range(n):
        if result[i][x] == 1:
            result[i][y] = 1
for i in result:
    print(*i)