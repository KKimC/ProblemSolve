from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
srr, src, sbr, sbc = 0, 0, 0, 0
hr, hc = 0, 0
dx1 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()
dir_dic = {0:"U",1:"R",2:"D",3:"L"}


def setting_const():
    global srr, src, sbr, sbc, shr, hc
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "R":
                srr, src = i, j
            if graph[i][j] == "B":
                sbr, sbc = i, j
            if graph[i][j] == "O":
                hr, hc = i, j


setting_const()


def check_b(kbr, kbc, krr, krc, llook):
    dr = dx1[llook][0]
    dc = dx1[llook][1]
    nr = kbr
    nc = kbc
    flag = True
    while graph[nr][nc] != "#":
        nr += dr
        nc += dc
        if graph[nr][nc] == "O":
            return (-1, -1)
        if nr == krr and nc == krc:
            flag = False
    if flag:
        return (nr - dr, nc - dc)
    else:
        return (nr - dr - dr, nc - dc - dc)


def check_a(krr, krc, kbr, kbc, llook):  # R의 경로를 탐색하는 함수 hole이면
    dr = dx1[llook][0]
    dc = dx1[llook][1]
    nr = krr
    nc = krc
    flag = True
    while graph[nr][nc] != "#":
        nr += dr
        nc += dc
        if graph[nr][nc] == "O":
            return (-1, -1)
        if nr == kbr and nc == kbc:
            flag = False
    if flag:
        return (nr - dr, nc - dc)
    else:
        return (nr - dr - dr, nc - dc - dc)


def move():
    q = deque([(srr, src, sbr, sbc, 0, 1,""), (srr, src, sbr, sbc, 0, 2,""), (srr, src, sbr, sbc, 0, 0,""),
               (srr, src, sbr, sbc, 0, 3,"")])
    visited.add((srr, src, sbr, sbc))
    while q:
        rr, rc, br, bc, depth, look, answer = q.popleft()
        for i in range(4):
            if i != look:
                nrr, nrc = check_a(rr, rc, br, bc, i)
                nbr, nbc = check_b(br, bc, rr, rc, i)
                if nrr == -1 and nbr == -1:
                    continue
                if nrr == -1:
                    return depth + 1
                if nbr == -1 and nbc == -1:
                    continue
                if 0 < nrr < n - 1 and 0 < nrc < m - 1 and 0 < nbr < n - 1 and 0 < nbc < m - 1 and (
                nrr, nrc, nbr, nbc) not in visited:
                    # todo r과 b를 따로 계산하여 r이나 b가 못가면 갈수 있는것만 움직이게 하는 기능 구현하기

                    visited.add((nrr, nrc, nbr, nbc))
                    q.append((nrr, nrc, nbr, nbc, depth + 1, i, answer+dir_dic[i]))


a = move()
if a:
    print(a)
else:
    print(-1)