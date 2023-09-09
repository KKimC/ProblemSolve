import sys
from collections import deque

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
tf_graph = [[False] * m for i in range(n)]
melt_q = deque()

def make_tf():  # TF_graph를 세팅해주는 함수
    global tf_graph
    for i in range (n):
        for j in range(m):
            if graph[i][j] != 0:
                tf_graph[i][j] = True
            
def check_split():  # 몇덩어리로 분리되어 있는지 체크하는 함수 0: 다녹음 1: 한덩어리 2: 두덩어리
    count = 0
    for i in range(n):
        for j in range(m):
            if count > 1:return 2
            if tf_graph[i][j]:
                tf_graph[i][j] = False
                count += 1
                q = deque([(i,j)])
                while q:
                    x,y = q.popleft()
                    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                        if 0<= x+dx < n:
                            if 0<= y+dy < m:
                                if tf_graph[x+dx][y+dy]:
                                    tf_graph[x+dx][y+dy] = False
                                    q.append((x+dx,y+dy))
    return count

def check_and_melt():
    qq = deque([])
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                cnt = 0
                for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                    if not graph[i+dx][j+dy]:
                        cnt += 1
                qq.append((i,j,cnt))
    while qq:
        i,j,cnt = qq.popleft()
        graph[i][j] = max(0,graph[i][j]-cnt)

make_tf()     
cs = check_split()
cnt = 0
while cs == 1:
    check_and_melt()
    make_tf()
    cs = check_split()
    cnt += 1
if cs != 0:
    print(cnt)
else:
    print(0)