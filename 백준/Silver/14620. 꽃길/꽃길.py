dx1 = [(-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1), (-2, 0), (0, 2), (2, 0), (0, -2)]
dx2 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def sum_flower(x, y):
    result = 0
    for dx, dy in dx2:
        result += graph[x+dx][y+dy]
    result += graph[x][y]
    return result

def make_false(x, y):
    visited[x][y] += 4
    for dx, dy in dx1:
        nx = x+dx
        ny = y+dy
        if 0<nx<n-1 and 0<ny<n-1:
            visited[nx][ny] += 1
def make_True(x, y):
    visited[x][y] -= 4
    for dx, dy in dx1:
        nx = x+dx
        ny = y+dy
        if 0<nx<n-1 and 0<ny<n-1:
            visited[nx][ny] -= 1


def blossom(x, y, depth, price): # 꽃심기 구현
    global minn
    if depth == 2:
        minn = min(minn,price+sum_flower(x,y))
        return
    make_false(x, y)
    for i in range(1,n-1):
        for j in range(1,n-1):
            if visited[i][j] < 1:
                blossom(i,j,depth+1,price+sum_flower(x,y))
    make_True(x,y)

minn = 10000
graph = []
n = int(input())

for _ in range(n):
    graph.append(list(map(int,input().split())))
for i in range(1,n-1):
    for j in range(1,n-1):
        visited = [[0] * n for _ in range(n)]
        blossom(i,j,0,0)
print(minn)
