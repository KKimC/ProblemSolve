def dfs(depth):
    if depth == len(word):
        print("".join(answer))
        return
    for k in hash:
        if hash[k]:
            hash[k] -= 1
            answer.append(k)
            dfs(depth + 1)
            hash[k] += 1
            answer.pop()


n = int(input())

for _ in range(n):
    word = sorted(list(input()))
    hash = {}
    answer = []
    for i in word:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    dfs(0)