n,l = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def check(arr):
    last = 0
    cnt = 1
    for idx,i in enumerate(arr):
        if cnt < 0:
            cnt += 1
            continue
        if last == 0:
            last = i
        else:
            if i>last+1 or i<last-1:
                return False
            if i == last:
                cnt += 1
                continue
            if i == last+1:
                if cnt >= l:
                    last= i
                    cnt = 1
                    continue
                else:
                    return False
            if i == last - 1:
                if n-idx < l:
                    return False
                else:
                    for j in range(1,l):
                        if arr[idx+j] != last-1:
                            return False
                    else:
                        last -= 1
                        cnt = -l+1

    return True

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(e) for e in list_of_tuples]

cnt = 0
for i in graph:
    if check(i):
        cnt += 1
for i in rotated(graph):
    if check(i):
        cnt += 1
print(cnt)
