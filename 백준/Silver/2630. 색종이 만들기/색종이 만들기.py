
nn = int(input())
graph = [ list(map(int,input().split())) for _ in range(nn)]
cnt_b = 0
cnt_w = 0

def judge(sx,sy, ex,ey, n):
    global cnt_b, cnt_w
    if sx == ex and sy == ey:
        if graph[sy][sx] == 1:
            cnt_b += 1
            return
        else:
            cnt_w += 1
            return
    a = 0
    for i in range(sx,ex+1):
        for j in range(sy, ey+1):
            if graph[j][i] == 0:
                a += 1
    
    if a == (n*2)*(n*2):
        cnt_w += 1
        return
    elif a == 0:
        cnt_b += 1
        return
    else:
        judge(sx,sy,sx+n-1,sy+n-1,n//2)
        judge(sx+n,sy,ex,sy+n-1,n//2)
        judge(sx,sy+n,sx+n-1,ey,n//2)
        judge(sx+n,sy+n,ex,ey,n//2)
        return

judge(0,0,nn-1,nn-1,nn//2)
print(cnt_w)
print(cnt_b)