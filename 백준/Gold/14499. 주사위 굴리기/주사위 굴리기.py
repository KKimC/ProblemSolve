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

    def find_bottom(self):
        return self.bottom

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

    def write_bottom(self,graph_val):
        self.bottom = graph_val



dice1 = dice(0,0,0,0,0,0)
n,m,x,y,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx1 = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
dice_actions = {1:dice1.turn_R(),2:dice1.turn_L(),3:dice1.turn_U(),4:dice1.turn_D()}
for i in map(int,input().split()):
    dx,dy = dx1[i]
    nx,ny = x+dx, y+dy
    if 0<=nx<n and 0<=ny<m:
        if i == 1:dice1.turn_R()
        if i == 2:dice1.turn_L()
        if i == 3:dice1.turn_U()
        if i == 4:dice1.turn_D()
        x, y = nx, ny
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice1.find_bottom()
        else:
            dice1.write_bottom(graph[nx][ny])
            graph[nx][ny] = 0
        print(dice1)