from collections import defaultdict

dc1 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
n = int(input())
dic_r = defaultdict(list)
dic_c = defaultdict(list)
INF = 99999999999
temp = INF
c = 0;r = 0
look = 1
def fun0():
    dic_c[c].append((r, rr))
def fun1():
    dic_r[r].append((cc, c))
def fun2():
    dic_c[c].append((rr, r))
def fun3():
    dic_r[r].append((c, cc))
def fun00(t):
    global r
    r -= t
def fun11(t):
    global c
    c += t
def fun22(t):
    global r
    r += t
def fun33(t):
    global c
    c -= t
def turn(l):
    global look
    if l == "R":
        look = (look + 1) % 4
    if l == "L":
        look = look-1 if look else 3
def check():
    global cnt, temp
    flag = False
    if look == 0:
        if c in dic_c:
            for x, y in dic_c[c]:
                if r <= y <= rr:
                    temp = min(temp, abs(rr-y))
                    flag = True
        for i in dic_r:
            if r <= i < rr:
                for j in dic_r[i]:
                    s, a = j
                    if s <= c <= a:
                        temp = min(abs(rr-i), temp)
                        flag = True
        if temp != INF: cnt += temp
        return flag
    if look == 1:
        if r in dic_r:
            for x, y in dic_r[r]:
                if cc <= x <= c:
                    temp = min(temp, abs(x-cc))
                    flag = True
        for i in dic_c:
            if cc < i <= c:
                for j in dic_c[i]:
                    s, a = j
                    if s <= r <= a:
                        temp = min(abs(cc-i), temp)
                        flag = True
        if temp != INF: cnt += temp
        return flag
    if look == 2:
        if c in dic_c:
            for x, y in dic_c[c]:
                if rr <= x <= r:
                    temp = min(temp, abs(x-rr))
                    flag = True
        for i in dic_r:
            if rr < i <= r:
                for j in dic_r[i]:
                    s, a = j
                    if s <= c <= a:
                        temp = min(abs(rr-i), temp)
                        flag = True
        if temp != INF: cnt += temp
        return flag
    if look == 3:
        if r in dic_r:
            for x, y in dic_r[r]:
                if c <= y <= cc:
                    temp = min(temp, abs(cc-y))
                    flag = True
        for i in dic_c:
            if c <= i < cc:
                for j in dic_c[i]:
                    s, a = j
                    if s <= r <= a:
                        temp = min(abs(cc-i), temp)
                        flag = True
        if temp != INF: cnt += temp
        return flag


dic_fun = {0: fun0, 1: fun1, 2: fun2, 3: fun3}
dic_fun1 = {0: fun00, 1: fun11, 2: fun22, 3: fun33}
cnt = 0
for i in range(int(input()) + 1):
    try:
        t, l = input().split()
    except:
        t, l = 2*n+1, "R"
    t = int(t)
    rr = r
    cc = c
    dic_fun1[look](t)
    if check():
        break
    if -n > r:
        cnt += abs(rr+n) + 1
        break
    if n < c:
        cnt += abs(cc-n) + 1
        break
    if n < r:
        cnt += abs(rr-n) + 1
        break
    if -n > c:
        cnt += abs(cc+n) + 1
        break
    cnt += t
    dic_fun[look]()
    turn(l)
print(cnt)