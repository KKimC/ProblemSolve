from collections import deque

for t in range(int(input())):
    nums = []
    start,final = map(int,input().split())
    mini_nums = [True] * 10001

    for i in range(2, 101):
        if mini_nums[i] == True:
            for j in range(i+i, 10001, i):
                mini_nums[j] = False
    for idx, ial in enumerate(mini_nums):
        if ial and idx>999:
            nums.append(idx)
    visited = [False]*len(nums)
    def poss(x,y):
        cnt = 0
        x = str(x)
        y = str(y)
        for i in range(4):
            if x[i] == y[i]:
                cnt += 1
        return True if cnt == 3 else False
    def bfs():
        idx = nums.index(start)
        visited[idx] = True
        q = deque([(start,1)])
        while q:
            iidx,depth = q.popleft()
            if iidx == final:
                return depth-1
            for jdx, jal in enumerate(nums):
                if poss(iidx,jal) and not visited[jdx]:
                    visited[jdx] = True
                    q.append((jal,depth+1))
    print(bfs())