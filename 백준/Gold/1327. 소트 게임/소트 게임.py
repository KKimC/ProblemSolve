from collections import deque

n,k = map(int, input().split())
graph = list(input().split())  # 3 2 1
visited = set(["".join(graph)])
target = "".join(map(str,range(1,n+1)))
q = deque()
q.append(["".join(graph), 0])
check = 0

def bfs():
    while q:
        arr, cnt = q.popleft()
        if arr == target:
            return cnt
        for i in range(n-k + 1):
            strs = arr[:i] + arr[i:i+k][::-1] + arr[i+k:]
            if strs not in visited:
                q.append([strs, cnt+1])
                visited.add(strs)
    else:
        return -1

print(bfs())