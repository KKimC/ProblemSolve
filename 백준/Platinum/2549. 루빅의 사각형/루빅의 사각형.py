from collections import deque
graph = [list(map(int,input().split())) for _ in range(4)]

def gprint(graph):
    for i in graph:
        print(f"{i[0]:2} {i[1]:2} {i[2]:2} {i[3]:2}")
    print()

def move_row1(graph,i):
    arr = [graph[0][:],graph[1][:],graph[2][:],graph[3][:]]
    arr[i] = [graph[i][3],graph[i][0],graph[i][1],graph[i][2]]
    return arr

def move_cal1(graph,j):
    arr = [graph[0][:], graph[1][:], graph[2][:], graph[3][:]]
    q = deque([])
    for k in range(4):
        q.append(arr[k][j])
    q.appendleft(q.pop())
    for k in range(4):
        arr[k][j] = q.popleft()
    return arr

def move_row2(graph,i):
    arr = [graph[0][:],graph[1][:],graph[2][:],graph[3][:]]
    arr[i] = [graph[i][2],graph[i][3],graph[i][0],graph[i][1]]
    return arr

def move_cal2(graph,j):
    arr = [graph[0][:], graph[1][:], graph[2][:], graph[3][:]]
    q = deque([])
    for k in range(4):
        q.append(arr[k][j])
    q.appendleft(q.pop())
    q.appendleft(q.pop())
    for k in range(4):
        arr[k][j] = q.popleft()
    return arr

def move_row3(graph,i):
    arr = [graph[0][:],graph[1][:],graph[2][:],graph[3][:]]
    arr[i] = [graph[i][1],graph[i][2],graph[i][3],graph[i][0]]
    return arr

def move_cal3(graph,j):
    arr = [graph[0][:], graph[1][:], graph[2][:], graph[3][:]]
    q = deque([])
    for k in range(4):
        q.append(arr[k][j])
    q.appendleft(q.pop())
    q.appendleft(q.pop())
    q.appendleft(q.pop())
    for k in range(4):
        arr[k][j] = q.popleft()
    return arr

def move(i,j):
    arr = [graph[0][:],graph[1][:],graph[2][:],graph[3][:]]
    arr[i] = [graph[i][3],graph[i][0],graph[i][1],graph[i][2]]
    q = deque([])
    for k in range(4):
        q.append(arr[k][j])
    q.appendleft(q.pop())
    for k in range(4):
        arr[k][j] = q.popleft()
    return arr

def check(arr):
    cnt = 0
    for i in range(4):
        for j in range(4):
            if arr[i][j] != 4*i+j+1:
                cnt += 1
    return cnt

visited_row = [False]*4
visited_cal = [False]*4
dic = {}

def dfs(result,depth,arr):
    global cnt
    chk = check(arr)
    if not chk:
        cnt = depth if depth < cnt else cnt
        if cnt not in dic:
            dic[cnt] = result
        return
    chk = chk // 4 + 1 if chk % 4 else chk // 4
    if chk > 7-depth:
        return
    if depth >= cnt:
        return
    if depth == 7:
        return
    for i in range(4):
        if not visited_row[i]:
            dfs(result+[(1,i+1,1)],depth+1,move_row1(arr,i))
            dfs(result+[(1,i+1,2)],depth+1,move_row2(arr,i))
            dfs(result+[(1,i+1,3)],depth+1,move_row3(arr,i))
        if not visited_cal[i]:
            dfs(result+[(2,i+1,1)],depth+1,move_cal1(arr,i))
            dfs(result+[(2,i+1,2)],depth+1,move_cal2(arr,i))
            dfs(result+[(2,i+1,3)],depth+1,move_cal3(arr,i))


cnt = 10
dfs([],0,graph)
print(cnt)
for i in dic[cnt]:
    print(*i)