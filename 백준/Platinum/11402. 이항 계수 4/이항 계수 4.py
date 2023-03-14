import sys

sys.setrecursionlimit(10**5)
def mpow(x, y):
    if x < y: return 0
    if not y or y == x: return 1
    if dp[x][y] != -1: return dp[x][y]
    dp[x][y] = mpow(x-1, y-1) % m + mpow(x-1, y) % m
    dp[x][y] %= m
    return dp[x][y]



n, r, m = map(int, input().split())
dp = [[-1] * (m+1) for _ in range(m+1)]
ret = 1
while n or r:
    ret *= mpow(n % m, r % m)
    ret %= m
    n //= m
    r //= m
print(ret)
