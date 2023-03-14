from sys import stdin

n, m = map(int, input().split())

tetris = []

for _ in range(n):
    tetris.append(list(map(int, stdin.readline().rstrip().split())))


# 1번 ----
def long(i, j, tetris):
    a = len(tetris)
    b = len(tetris[0])

    if 0 <= i < a and 0 <= j+3 < b:
        one = tetris[i][j]
        two = tetris[i][j+1]
        three = tetris[i][j+2]
        four = tetris[i][j+3]
        return (one + two + three + four)
    else:
        return 0


# 2번 정사각형
def rect(i, j, tetris):
    a = len(tetris)
    b = len(tetris[0])

    if 0 <= i+1 < a and 0 <= j+1 < b:
        one = tetris[i][j]
        two = tetris[i][j+1]
        three = tetris[i+1][j]
        four = tetris[i+1][j+1]
        return (one + two + three + four)
    else:
        return 0


# 3번 L
def el(i, j, tetris):
    a = len(tetris)
    b = len(tetris[0])

    if 0 <= i + 2 < a and 0 <= j+1 < b:
        one = tetris[i][j]
        two = tetris[i+1][j]
        three = tetris[i+2][j]
        four = tetris[i+2][j+1]
        return (one + two + three + four)
    else:
        return 0


# 4번 번개
def thun(i, j, tetris):
    a = len(tetris)
    b = len(tetris[0])

    if 0 <= i+2 < a and 0 <= j + 1 < b:
        one = tetris[i][j]
        two = tetris[i+1][j]
        three = tetris[i+1][j+1]
        four = tetris[i+2][j+1]
        return (one + two + three + four)
    else:
        return 0


# 5번 산
def moun(i, j, tetris):
    a = len(tetris)
    b = len(tetris[0])

    if 0 <= i+1 < a and 0 <= j+2 < b:
        one = tetris[i][j]
        two = tetris[i][j+1]
        three = tetris[i][j+2]
        four = tetris[i+1][j+1]
        return (one + two + three + four)
    else:
        return 0


# 왼쪽으로 돌리는 그래프
def turn_right(tetris):

    # tetris = [[a]*y for _ in range(x)]

    # row
    x = len(tetris)
    # col
    y = len(tetris[0])

    new_tetris = [[0]*x for i in range(y)]

    for i in range(x):
        for j in range(y):
            new_tetris[y-j-1][i] = tetris[i][j]

    return new_tetris


def zau(tetris):
    # row
    x = len(tetris)
    # col
    y = len(tetris[0])

    new_tetris = [[0]*y for _ in range(x)]

    for i in range(x):
        for j in range(y):
            new_tetris[i][y-j-1] = tetris[i][j]

    return new_tetris


d = 0
max_value = 0


while d <= 3:
    for i in range(len(tetris)):
        for j in range(len(tetris[0])):
            cnt_1 = long(i, j, tetris)
            cnt_2 = rect(i, j, tetris)
            cnt_3 = el(i, j, tetris)
            cnt_4 = thun(i, j, tetris)
            cnt_5 = moun(i, j, tetris)
            value = max(cnt_1, cnt_2, cnt_3, cnt_4, cnt_5)
            if value > max_value:
                max_value = value

    new = zau(tetris)
    for i in range(len(new)):
        for j in range(len(new[0])):
            cnt_1 = long(i, j, new)
            cnt_2 = rect(i, j, new)
            cnt_3 = el(i, j, new)
            cnt_4 = thun(i, j, new)
            cnt_5 = moun(i, j, new)
            value = max(cnt_1, cnt_2, cnt_3, cnt_4, cnt_5)
            if value > max_value:
                max_value = value

    tetris = zau(new)

    # tetris를 turn_right함
    tetris = turn_right(tetris)
    d += 1


print(max_value)
