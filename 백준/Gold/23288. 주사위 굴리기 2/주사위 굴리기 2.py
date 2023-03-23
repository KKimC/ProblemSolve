from collections import deque
class dice:
    def __init__(self, bottom, R,L,U,D, top):
        self.bottom = bottom
        self.R = R
        self.L = L
        self.U = U
        self.D = D
        self.top = top

    def __str__(self):
        return str(self.top)

    def turn_L(self):
        temp = self.bottom
        self.bottom = self.L
        self.L = self.top
        self.top = self.R
        self.R = temp

    def turn_R(self):
        temp = self.bottom
        self.bottom = self.R
        self.R = self.top
        self.top = self.L
        self.L = temp

    def turn_U(self):
        temp = self.bottom
        self.bottom = self.U
        self.U = self.top
        self.top = self.D
        self.D = temp

    def turn_D(self):
        temp = self.bottom
        self.bottom = self.D
        self.D = self.top
        self.top = self.U
        self.U = temp


dx1 = [(-1,0),(0,1),(1,0),(0,-1)]
n,m,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dice_look = 1
x = 0
y = 0
score = 0
dice1 = dice(6,3,4,2,5,1)
dice_actions = {0:dice1.turn_U,1:dice1.turn_R,2:dice1.turn_D,3:dice1.turn_L}

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = True
    cnt = 0
    while q:
        xx,yy= q.popleft()
        cnt += 1
        for dx,dy in dx1:
            nx = xx+dx
            ny = yy+dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
    return cnt
score_graph = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited = [[False]*m for _ in range(n)]
        score_graph[i][j] = bfs(i,j)

for i in range(k):
    if 0<=x+dx1[dice_look][0]<n and 0<= y+dx1[dice_look][1]<m:
        score += score_graph[x+dx1[dice_look][0]][y+dx1[dice_look][1]] * graph[x+dx1[dice_look][0]][y+dx1[dice_look][1]]
        dice_actions[dice_look]()
        x += dx1[dice_look][0]
        y += dx1[dice_look][1]
        if dice1.bottom > graph[x][y]:
            dice_look = dice_look+1 if dice_look<3 else 0
        elif graph[x][y] > dice1.bottom:
            dice_look = dice_look-1 if dice_look>0 else 3
    else:
        dice_look = (dice_look+2)%4
        score += score_graph[x + dx1[dice_look][0]][y + dx1[dice_look][1]] * graph[x + dx1[dice_look][0]][y + dx1[dice_look][1]]
        dice_actions[dice_look]()
        x += dx1[dice_look][0]
        y += dx1[dice_look][1]
        if dice1.bottom > graph[x][y]:
            dice_look = dice_look + 1 if dice_look < 3 else 0
        elif graph[x][y] > dice1.bottom:
            dice_look = dice_look - 1 if dice_look > 0 else 3
print(score)
