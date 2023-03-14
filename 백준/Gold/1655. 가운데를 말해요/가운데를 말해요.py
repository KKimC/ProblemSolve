import heapq
import sys

n = int(input())
result_f = []
fcnt=  0
result_b = []
bcnt = 0


for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if len(result_f) == len(result_b):
        heapq.heappush(result_f,(-a,a))
    else:
        heapq.heappush(result_b,a)
    if result_b and result_f[0][1] > result_b[0]:
        minn = heapq.heappop(result_b)
        maxx = heapq.heappop(result_f)[1]
        heapq.heappush(result_f, (-minn,minn))
        heapq.heappush(result_b,maxx)
    print(result_f[0][1])