def one():
    global look,look1
    mini[0][0], mini[1][0] = mini[1][0], mini[0][0]
    mini[0][1], mini[1][1] = mini[1][1], mini[0][1]
    if look == 0:look = 2
    elif look == 2:look = 0
    if look1 == 0:look1 = 2
    elif look1 == 2:look1 = 0


def two():
    global look,look1
    mini[0][0], mini[0][1] = mini[0][1], mini[0][0]
    mini[1][0], mini[1][1] = mini[1][1], mini[1][0]
    if look == 1: look = 3
    elif look == 3: look = 1
    if look1 == 1: look1 = 3
    elif look1 == 3: look1 = 1


def three():
    global look, look1
    a = mini[0][0]
    b = mini[0][1]
    c = mini[1][0]
    d = mini[1][1]
    mini[0][0] = c
    mini[0][1] = a
    mini[1][0] = d
    mini[1][1] = b
    if look == 0:
        look = 1
    elif look == 1:
        look = 2
    elif look == 2:
        look = 3
    elif look == 3:
        look = 0
    if look1 == 0:
        look1 = 1
    elif look1 == 1:
        look1 = 2
    elif look1 == 2:
        look1 = 3
    elif look1 == 3:
        look1 = 0


def four():
    global look,look1
    a = mini[0][0]
    b = mini[0][1]
    c = mini[1][0]
    d = mini[1][1]
    mini[0][0] = b
    mini[0][1] = d
    mini[1][0] = a
    mini[1][1] = c
    if look == 0:
        look = 3
    elif look == 1:
        look = 0
    elif look == 2:
        look = 1
    elif look == 3:
        look = 2
    if look1 == 0:
        look1 = 3
    elif look1 == 1:
        look1 = 0
    elif look1 == 2:
        look1 = 1
    elif look1 == 3:
        look1 = 2


def five():
    a = mini[0][0]
    b = mini[0][1]
    d = mini[1][0]
    c = mini[1][1]
    mini[0][0] = d
    mini[0][1] = a
    mini[1][0] = c
    mini[1][1] = b


def six():
    a = mini[0][0]
    b = mini[0][1]
    d = mini[1][0]
    c = mini[1][1]
    mini[0][0] = b
    mini[0][1] = c
    mini[1][0] = a
    mini[1][1] = d

def oneone(graph2):
    n = len(graph2)
    m = len(graph2[0])
    for i in range(n//2):
        arr = graph2[i][:]
        for j in range(m):
            graph2[i][j] = graph2[n-1-i][j]
        for j in range(m):
            graph2[n-1-i][j] = arr[j]
def twotwo(graph2):
    n = len(graph2)
    m = len(graph2[0])
    for i in range(m//2):
        arr = []
        for j in range(n):
            arr.append(graph2[j][i])
        for j in range(n):
            graph2[j][i] = graph2[j][m-i-1]
        for j in range(n):
            graph2[j][m-i-1] = arr[j]


look = 0
look1 = 3
n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
mini = [[1, 2], [3, 4]]
dic = {1: one, 2: two, 3: three, 4: four, 5: five, 6: six}
for i in map(int, input().split()):
    dic[i]()
arr_1 = []
for i in range(0, n // 2):
    arr_1.append(graph[i][:m // 2])
arr_2 = []
for i in range(0, n // 2):
    arr_2.append(graph[i][m // 2:])
arr_3 = []
for i in range(n // 2, n):
    arr_3.append(graph[i][:m // 2])
arr_4 = []
for i in range(n // 2, n):
    arr_4.append(graph[i][m // 2:])
a = mini[0][0]
b = mini[0][1]
c = mini[1][0]
d = mini[1][1]

for i in range(look):
    arr_1 = list(map(list, zip(*arr_1[::-1])))
    arr_2 = list(map(list, zip(*arr_2[::-1])))
    arr_3 = list(map(list, zip(*arr_3[::-1])))
    arr_4 = list(map(list, zip(*arr_4[::-1])))
if look == 0:
    if look1 == 1:
        twotwo(arr_1)
        twotwo(arr_2)
        twotwo(arr_3)
        twotwo(arr_4)
elif look == 1:
    if look1 == 2:
        oneone(arr_1)
        oneone(arr_2)
        oneone(arr_3)
        oneone(arr_4)
elif look == 2:
    if look1 == 3:
        twotwo(arr_1)
        twotwo(arr_2)
        twotwo(arr_3)
        twotwo(arr_4)
elif look == 3:
    if look1 == 0:
        oneone(arr_1)
        oneone(arr_2)
        oneone(arr_3)
        oneone(arr_4)

dicc = {1: arr_1, 2: arr_2, 3: arr_3, 4: arr_4}

nn = len(arr_1)
mm = len(arr_1[0])
result = []
for i in range(nn):
    result.append(dicc[a][i] + dicc[b][i])
for i in range(nn):
    result.append(dicc[c][i] + dicc[d][i])
for i in result:
    print(*i)