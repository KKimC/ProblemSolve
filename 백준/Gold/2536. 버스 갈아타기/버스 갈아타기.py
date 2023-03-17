if True:
    import sys
    from collections import deque
    m,n = map(int,sys.stdin.readline().rstrip().split())
    nbus = int(sys.stdin.readline().rstrip())
    dic_bus = {}
    for i in range(nbus):
        bus_num,r,c,rr,cc = map(int,sys.stdin.readline().rstrip().split())
        if r == rr:
            if c>cc:c,cc = cc,c
            dic_bus[bus_num] = ("r",r,(c,cc))
        else:
            if r>rr:r,rr = rr,r
            dic_bus[bus_num] = ("c",c,(r,rr))
    st_r,st_c,ar_r,ar_c = map(int,sys.stdin.readline().rstrip().split())
    q = deque([])
    visited = [False]*(nbus+1)
    target = set()
    for i in range(1,bus_num+1):
        if dic_bus[i][0] == "r":
            if dic_bus[i][1] == ar_r and dic_bus[i][2][0]<= ar_c <= dic_bus[i][2][1]:
                target.add(i)
        if dic_bus[i][0] == "c":
            if dic_bus[i][1] == ar_c and dic_bus[i][2][0]<= ar_r <= dic_bus[i][2][1]:
                target.add(i)
    for i in range(1,bus_num+1):
        if dic_bus[i][0] == "r":
            if dic_bus[i][1] == st_r and dic_bus[i][2][0]<= st_c <= dic_bus[i][2][1]:
                visited[i] = True
                q.append((i,1))
        if dic_bus[i][0] == "c":
            if dic_bus[i][1] == st_c and dic_bus[i][2][0]<= st_r <= dic_bus[i][2][1]:
                visited[i] = True
                q.append((i,1))
    while q:
        bus,cnt = q.popleft()
        if bus in target:
            print(cnt)
            break
        i = bus
        for j in range(1,nbus+1):
            if not visited[j]:
                if dic_bus[i][0] == "r" and dic_bus[j][0] == "r":
                    if dic_bus[i][1] == dic_bus[j][1] and ((dic_bus[j][2][0]<= dic_bus[i][2][0] <= dic_bus[j][2][1]) or (dic_bus[j][2][0]<= dic_bus[i][2][1] <= dic_bus[j][2][1]) or (dic_bus[i][2][0]<= dic_bus[j][2][1] <= dic_bus[i][2][1]) or (dic_bus[i][2][0]<= dic_bus[j][2][0] <= dic_bus[i][2][1])):
                        visited[j] = True
                        q.append((j,cnt+1))
                if dic_bus[i][0] == "r" and dic_bus[j][0] == "c":
                    if dic_bus[j][2][0]<= dic_bus[i][1] <= dic_bus[j][2][1] and dic_bus[i][2][0]<= dic_bus[j][1] <= dic_bus[i][2][1]:
                        visited[j] = True
                        q.append((j,cnt+1))
                if dic_bus[i][0] == "c" and dic_bus[j][0] == "c":
                    if dic_bus[i][1] == dic_bus[j][1] and ((dic_bus[j][2][0]<= dic_bus[i][2][0] <= dic_bus[j][2][1]) or (dic_bus[j][2][0]<= dic_bus[i][2][1] <= dic_bus[j][2][1]) or (dic_bus[i][2][0]<= dic_bus[j][2][1] <= dic_bus[i][2][1]) or (dic_bus[i][2][0]<= dic_bus[j][2][0] <= dic_bus[i][2][1])):
                        visited[j] = True
                        q.append((j,cnt+1))
                if dic_bus[i][0] == "c" and dic_bus[j][0] == "r":
                    if dic_bus[j][2][0] <= dic_bus[i][1] <= dic_bus[j][2][1] and dic_bus[i][2][0] <= dic_bus[j][1] <= dic_bus[i][2][1]:
                        visited[j] = True
                        q.append((j,cnt+1))