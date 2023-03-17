n,m,xx = map(int,input().split())

import heapq  # 우선순위 큐 구현을 위함
from collections import defaultdict

graphh = defaultdict(dict)
for i in range(m):
    x,y,t = map(int,input().split())
    graphh[x][y] = t

def dijkstra(graph, start):
    d = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
    d[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [d[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if d[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < d[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                d[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return d

maxx = 0
key = 0
dikc = dijkstra(graphh,xx)
lst = [0]*(n+1)
for i in range(1,n+1):
    lst[i] = dijkstra(graphh,i)[xx]
for i in range(1,n+1):
    lst[i] += dikc[i]
print(max(lst))