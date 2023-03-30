def left(x,y):
    return x-1,y
def right(x,y):
    return x+1,y
def up(x,y):
    return x,y-1
def down(x,y):
    return x,y+1
def marking(x,y,d,g):
    d = direction[d]
    visited[x][y] = True
    dx = x
    dy = y
    for i in dps[d][g]:
        nx,ny = move[i](dx,dy)
        if 0<=nx<101 and 0<=ny<101:
            visited[nx][ny] = True
        dx = nx
        dy = ny
def checking(x,y):
    if visited[x+1][y] and visited[x][y+1] and visited[x+1][y+1]:
        return True
    else:
        return False


direction = {0:"2",1:"3",2:"1",3:"4"}
move = {"1":left,"2":right,"3":up,"4":down}
next_move = {'2':'3','3':'1','1':'4',"4":"2"}
dps = {}
visited = [[False]*101 for _ in range(101)]
cnt = 0


for k in "1234":
    dp = [""] * 11
    dp[0] = k
    dp[1] = k + next_move[k]
    for i in range(2,11):
        temp = dp[i-1]
        for j in dp[i-1][::-1]:
            temp += next_move[j]
        dp[i] = temp
    dps[k] = dp

for _ in range(int(input())):
    marking(*map(int,input().split()))
for i in range(100):
    for j in range(100):
        if visited[i][j]:
            if checking(i,j):
                cnt += 1
print(cnt)





