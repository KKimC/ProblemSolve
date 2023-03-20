n = int(input())
graph = list(map(int,input().split()))
sum_money = int(input())
start = 1
end = max(graph)

def sum_graph(money):
    result = 0
    for i in graph:
        if i <= money:
            result += i
        else:
            result += money
    return result

result = 0
while start <= end:
    mid = (start + end) // 2
    temp = sum_graph(mid)
    if temp > sum_money:
        end = mid-1
    if temp <= sum_money:
        result = mid
        start = mid+1
print(result)