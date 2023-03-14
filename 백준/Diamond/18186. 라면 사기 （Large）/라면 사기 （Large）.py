n,b,c = map(int,input().split())
graph = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0
cnt3 = 0

if b<=c:
    print(sum(graph)*b)
else:
    

    for i in range(n - 2):
        t1 = 0
        t2 = 0
        t3 = 0
        if graph[i+2] > graph[i+1]:
            t3 = min(graph[i],graph[i+1],graph[i+2])
            graph[i] -= t3
            graph[i+1] -= t3
            graph[i+2] -= t3
            t2 = min(graph[i],graph[i+1])
            graph[i] -= t2
            graph[i+1] -= t2
            t1 = graph[i]
            graph[i] = 0
            cnt1+=t1
            cnt2+=t2
            cnt3+=t3
        else:
            if graph[i+1]-graph[i+2] >= graph[i]:
                t2 += graph[i]
                graph[i] = 0
                graph[i+1] -= t2
                cnt2 += t2
            else:
                t2 = graph[i+1]-graph[i+2]
                t3 = min(graph[i+2],graph[i]-t2)
                graph[i+2] -= t3
                graph[i+1] -= t2+t3
                graph[i] -= t2+t3
                t1 = graph[i]
                graph[i] = 0
                cnt1+=t1
                cnt2+=t2
                cnt3+=t3


    if not graph[-2]:
        cnt1 = cnt1 + graph[-1]

    else:
        if graph[-1] == graph[-2]:
            cnt2 += graph[-1]
        elif graph[-1] > graph[-2]:
            cnt2 += graph[-2]
            cnt1 += graph[-1] - graph[-2]
        else:
            cnt2 += graph[-1]
            cnt1 += graph[-2] - graph[-1]
    print(cnt1 * (b) + cnt2 * (b+c) + cnt3 * (b+2*c))