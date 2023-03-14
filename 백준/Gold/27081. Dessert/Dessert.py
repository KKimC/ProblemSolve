n = int(input())
dic = {}
for i in range(1,n+1):
    arr = ""
    for j in range(i,n+1):
       arr += str(j)
    dic[i] = int(arr)
dic[n+1] = 0
dic[0] = 0
cnt = 0
result = []
def dfs(depth,stk,stk_prt,res,prt):
    global cnt
    if depth == n+1:
        if not res + stk:
            result.append(prt + " + " + stk_prt)
            cnt += 1
        if not res - stk:
            result.append(prt + " - " + stk_prt)
            cnt += 1
        return
    if res > dic[depth-1]:
        return
    if prt:
        dfs(depth+1,depth,str(depth),res+stk,prt+" + "+stk_prt)
        dfs(depth+1,depth,str(depth),res-stk,prt+" - "+stk_prt)
        dfs(depth+1, int(str(stk) + str(depth)), stk_prt + " . " + str(depth), res, prt)
    else:
        dfs(depth + 1, depth, str(depth), res + stk,stk_prt)
        dfs(depth + 1, int(str(stk) + str(depth)), stk_prt + " . " + str(depth), res, prt)
dfs(2,1,"1",0,"")
for i in sorted(result)[:20]:
    print(i)
print(cnt)
