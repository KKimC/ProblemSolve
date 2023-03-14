if True:
    def dfs(depth):
        global result
        if depth == 15:
            result = 1
            for i in graph:
                for j in i:
                    if j:
                        result = 0
                        return
            return
        for i in range(1,4):
            x,y = dic_check[i]
            team_1 = lst[depth][0]
            team_2 = lst[depth][1]
            if graph[team_1][x] * graph[team_2][y]:
                graph[team_1][x] -= 1
                graph[team_2][y] -= 1
                dfs(depth+1)
                graph[team_1][x] += 1
                graph[team_2][y] += 1
    result_table = []
    lst = []
    dic_check = {1: (0, 2), 2: (1, 1), 3: (2, 0)}
    for i in range(6):
        for j in range(i+1,6):
            lst.append((i,j))
    for _ in range(4):
        graph = []
        mscr = []
        for idx, ial in enumerate(map(int, input().split())):
            mscr.append(ial)
            if len(mscr) == 3:
                graph.append(mscr)
                mscr = []
        result = 0
        dfs(0)
        result_table.append(result)

    print(*result_table)