from collections import defaultdict

def dfs(depth,arr):
    global flag
    if depth == n:
        if flag:
            for x,y,i in arr:
                graph[x][y] = i
            flag = False
        return
    x,y = zero_lst[depth]
    for i in range(1,10):
        if i not in row_hash[x] and i not in col_hash[y] and i not in sq_hash[find_number(x,y)] and flag:
            add_set(x,y,i)
            dfs(depth+1,arr+[(x,y,i)])
            remove_set(x,y,i)
    else:
        return


def find_number(x,y):
    if 0<=x<3 and 0<=y<3:return 1
    elif 3<=x<6 and 0<=y<3:return 2
    elif 6<=x<9 and 0<=y<3:return 3
    elif 0<=x<3 and 3<=y<6:return 4
    elif 3<=x<6 and 3<=y<6:return 5
    elif 6<=x<9 and 3<=y<6:return 6
    elif 0<=x<3 and 6<=y<9:return 7
    elif 3<=x<6 and 6<=y<9:return 8
    elif 6<=x<9 and 6<=y<9:return 9

def add_set(x,y,i):
    row_hash[x].add(i)
    col_hash[y].add(i)
    sq_hash[find_number(x,y)].add(i)

def remove_set(x,y,i):
    row_hash[x].remove(i)
    col_hash[y].remove(i)
    sq_hash[find_number(x,y)].remove(i)


graph = [list(map(int,input())) for _ in range(9)]
row_hash = defaultdict(set)
col_hash = defaultdict(set)
sq_hash = defaultdict(set)
zero_lst = []

for idx,val in enumerate(graph):
    for jdx,jal in enumerate(val):
        if jal:
            sq_hash[find_number(idx,jdx)].add(jal)
            row_hash[idx].add(jal)
            col_hash[jdx].add(jal)
        else:
            zero_lst.append((idx,jdx))

cnt = 0
n = len(zero_lst)
flag = True

dfs(0,[])
for i in graph:
    print(*i,sep="")
