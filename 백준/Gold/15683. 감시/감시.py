n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx1 = [(-1,0),(0,1),(1,0),(0,-1)]

def one(x,y,look, k):
    look = look%4
    while 0<=x<n and 0<=y<m and graph[x][y] != 6:
        if graph[x][y] <= 0:
            graph[x][y] -= k
        x += dx1[look][0]
        y += dx1[look][1]

def two(x,y,look, k):
    one(x,y,look, k)
    one(x,y,look+2, k)

def three(x,y,look, k):
    one(x,y,look, k)
    one(x,y,look+1,k)

def four(x,y,look, k):
    one(x,y,look, k)
    one(x,y,look+1, k)
    one(x,y,look+2, k)

def five(x,y,look, k):
    for i in range(4):
        one(x,y,i,k)

fun_dic = {1:one,2:two,3:three,4:four,5:five}
maxx = 65
def dfs(i):
    global maxx
    if i == len(q):
        count = 0
        for idx in graph:
            for j in idx:
                if not j:
                    count += 1
        maxx = min(count,maxx)
        return
    for j in range(4):
        fun_dic[q[i][2]](q[i][0],q[i][1],j,1)
        dfs(i+1)
        fun_dic[q[i][2]](q[i][0],q[i][1],j,-1)


q = []
for idx,ial in enumerate(graph):
    for jdx,jal in enumerate(ial):
        if 0<jal<6:
            q.append((idx,jdx,jal))
dfs(0)
print(maxx)
