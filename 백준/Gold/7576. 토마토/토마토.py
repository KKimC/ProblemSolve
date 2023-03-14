from collections import deque

dx = [-1, 1, 0, 0] # 토마토의 사방이 익으므로
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def tomato(q): # 토마토의 초기 좌표를 받아서 익힐수 있는 마지막 토마토까지 익혀서 그 날짜를 반환하는 함수
    maxx = 0 # 반환할 day

    while q: # 확인해야할 좌표를 담은 큐
        xx, yy, tt = q.popleft() # 큐 내부에는 토마토의 위치 정보와 그 토마토가 몇일차에 익었는지를 담아둠
        for i in range(4): # 상하좌우 사방으로 탐색하면서
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 만약 탐색 범위를 넘어가지 않고
                if graph[nx][ny] == 0: # 익지않은 토마토라면
                    graph[nx][ny] = 1 # 토마토를 일단 익히고
                    q.append((nx, ny, tt + 1)) # 그 토마토는 익었으니까 사방을 탐색해야하므로 큐에 추가
                    if maxx < tt + 1:
                        maxx = tt + 1 # 날짜 + 1
    return maxx


aa = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            aa.append((i, j, 0)) # 처음에 토마토가 어디에 있었는지 큐에 추가
AA = tomato(aa) # 처음에 있는 토마토부터 익히기 시작함
for i in range(n): # 충분히 시간이 지났을때 그래프를 순회하면서
    if 0 in graph[i]: # 만약 안익은 토마토가 있다면
        print(-1)
        break
else: # 안익은 토마토가 없다면 날짜 출력
    print(AA)