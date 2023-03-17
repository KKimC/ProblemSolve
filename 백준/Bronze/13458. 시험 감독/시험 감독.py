n = int(input())
people = list(map(int,input().split()))
b,c = map(int,input().split())
cnt = 0
for i in people:
    if i > b:
        if not (i-b)%c:
            cnt += (i-b)//c
        else:
            cnt += (i-b)//c+1
    cnt += 1
print(cnt)