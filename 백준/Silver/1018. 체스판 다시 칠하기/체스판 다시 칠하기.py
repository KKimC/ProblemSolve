def find_color(x, y, color):
    count = 0
    color2 = "B" if color == "W" else "W"
    for i in range(8):
        for j in range(0, 8, 2):
            if i % 2 == 0:
                if color != graph[x + i][y + j]:
                    count += 1
            else:
                if color != graph[x + i][y + j+ 1]:
                    count += 1
            if i % 2 == 0:
                if color2 != graph[x + i][y + j + 1]:
                    count += 1
            else:
                if color2 != graph[x + i][y + j]:
                    count += 1
    return count

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(input())
table = []
for i in range(n - 7):
    for j in range(m - 7):
        table.append(min(find_color(i, j, "W"), find_color(i, j, "B")))
print(min(table))