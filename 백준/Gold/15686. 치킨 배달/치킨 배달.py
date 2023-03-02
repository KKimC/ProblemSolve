n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]


def cal_ch(ch_i):
    result = 0
    for hx, hy in ho:
        minn = 987654321
        for cx,cy in ch_i:
            a = abs(hx - cx) + abs(hy - cy)
            if minn > a: minn = a
        result += minn
    return result


def dfs(x,depth,sum_ch):
    global min_sum
    if depth == m-1:
        if cal_ch(sum_ch) < min_sum:
            min_sum = cal_ch(sum_ch)
        return
    for i in range(x+1,len(ch)):
        dfs(i,depth+1,sum_ch+[ch[i]])


ch = []
ho = []
result_arr = []
min_sum = 987654321
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ho.append((i,j))
        if graph[i][j] == 2:
            ch.append((i,j))
for i in range(len(ch)):
    dfs(i,0,[ch[i]])

print(min_sum)
