import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    count = 1
    set_queue = set([(0, 0, graph[0][0])])

    while set_queue:
        x, y, alpabet = set_queue.pop()
        count = max(count, len(alpabet))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in alpabet:
                set_queue.add((nx, ny, graph[nx][ny] + alpabet))
    print(count)


bfs()
