N = input() # 첫번째 문자 가로
M = input() # 두번째 문자 세로

# print(M[0],M[1])

a,b = len(N),len(M)

graph = [[0]*(a+1) for _ in range(b+1)]

arr = []
for col in range(1,b+1):
    for row in range(1,a+1):
        if M[col-1] == N[row-1]:
            graph[col][row] = graph[col-1][row-1]+1

        else:
            graph[col][row] = max(graph[col][row-1],graph[col-1][row])

print(graph[col][row])
y,x = b,a # 세로,가로

while y>0 and x>0:
    if graph[y-1][x] == graph[y][x]:
        y-=1
    elif graph[y][x-1] == graph[y][x]:
        x-=1
    else:
        x-=1
        y-=1
        arr.append(M[y])

for i in arr[::-1]:
    print(i,end="")