from collections import deque

dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
n = int(input())
graph = [[0]*n for i in range(n)]

visited = [[0]*n for i in range(n)]

def find_friends(lst):
    result = []
    for i in range(n):
        for j in range(n):
            result1 = 0
            result2 = 0
            if graph[i][j]:continue
            for dx,dy in dx1:
                nx = i+dx
                ny = j+dy
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] in lst:
                        result1 += 1
                    if not graph[nx][ny]:
                        result2 += 1
            result.append([result1,result2,-i,-j])
    return max(result)

like = 0
def count_cnt(x,y,lst):
    result = 0
    for dx,dy in dx1:
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] in lst:
            result += 1
    return result
dic = {}
for _ in range(n**2):
    a,b,c,d,e = map(int,input().split())
    dic[a] = {b,c,d,e}
    _,_,x,y = find_friends({b,c,d,e})
    graph[-x][-y] = a

for i in range(n):
    for j in range(n):
        cnt = count_cnt(i,j,dic[graph[i][j]])
        like += 10**(cnt-1) if cnt > 0 else 0

print(like)