from copy import deepcopy

n, m, k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    if m != 0:
        graph[r - 1][c - 1].append([m, s, d])
dy1 = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
for _ in range(k):
    n_graph = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] != []:
                for b in range(len(graph[x][y])):
                    nm, ns, nd = graph[x][y][b]
                    nx, ny = x + dy1[nd][0] * ns, y + dy1[nd][1] * ns
                    ny = (ny + n) % n
                    nx = (nx + n) % n
                    n_graph[nx][ny].append([nm, ns, nd])
    for xx in range(n):
        for yy in range(n):
            if len(n_graph[xx][yy]) > 1:
                cm, cs, cd = 0, 0, []
                cnt = len(n_graph[xx][yy])
                for c in range(cnt):
                    cm += n_graph[xx][yy][c][0]
                    cs += n_graph[xx][yy][c][1]
                    cd.append(n_graph[xx][yy][c][2] % 2)
                cm = int(cm / 5)
                cs = int(cs / cnt)
                n_graph[xx][yy] = []
                if cm != 0:
                    if sum(cd) == 0 or sum(cd) == cnt:
                        for i in range(4):
                            n_graph[xx][yy].append([cm, cs, i * 2])
                    else:
                        for j in range(4):
                            n_graph[xx][yy].append([cm, cs, j * 2 + 1])
    graph = deepcopy(n_graph)
sum_m = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] != []:
            for b in range(len(graph[x][y])):
                sum_m += graph[x][y][b][0]
print(sum_m)