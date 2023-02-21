def one():
    for i in range(n//2):
        arr = graph[i][:]
        for j in range(m):
            graph[i][j] = graph[n-1-i][j]
        for j in range(m):
            graph[n-1-i][j] = arr[j]
def two():
    for i in range(m//2):
        arr = []
        for j in range(n):
            arr.append(graph[j][i])
        for j in range(n):
            graph[j][i] = graph[j][m-i-1]
        for j in range(n):
            graph[j][m-i-1] = arr[j]


def three():
    global graph, n, m
    graph = list(map(list, zip(*graph[::-1])))
    n,m = m,n


def four():
    global graph, n, m
    graph = list(map(list, zip(*graph)))[::-1]
    n, m = m, n

def five():
    nn = n // 2
    mm = m // 2
    arr = []
    for i in range(nn):
        arr.append(graph[i][0:mm])

    for i in range(0, nn):
        for j in range(0, mm):
            graph[i][j] = graph[i+nn][j]

    for i in range(nn, n):
        for j in range(0, mm):
            graph[i][j] = graph[i][j-mm]

    for i in range(nn, n):
        for j in range(mm, m):
            graph[i][j] = graph[i-nn][j]

    for i in range(0, nn):
        for j in range(mm, m):
            graph[i][j] = arr[i][j-mm]

def six():
    nn = n//2
    mm = m//2
    arr = []
    for i in range(nn):
        arr.append(graph[i][0:mm])
    for i in range(0,nn):
        for j in range(0,mm):
            graph[i][j] = graph[i][j+mm]
    for i in range(0,nn):
        for j in range(mm,m):
            graph[i][j] = graph[i+nn][j]
    for i in range(nn,n):
        for j in range(mm,m):
            graph[i][j] = graph[i][j-mm]
    for i in range(nn,n):
        for j in range(0,mm):
            graph[i][j] = arr[i-nn][j]


n,m,r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dic = {1:one, 2:two, 3:three, 4:four, 5:five, 6:six}
for i in map(int,input().split()):
    dic[i]()
for i in graph:
    print(*i)