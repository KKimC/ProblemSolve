n, k = map(int, input().split())

hole = []
lt = list(map(int, input().split(" ")))


def findmin(left_idx):
    fmlst = lt[left_idx:]
    lt_max = 0
    cnttt = 0
    for idx, val in enumerate(hole):
        try:
            if lt_max < fmlst.index(val):
                lt_max = fmlst.index(val)
                cnttt = idx
        except:
            return idx
    return cnttt


count = 0
hcnt = 0
for idx, val in enumerate(lt):
    if val in hole:
        continue
    if hcnt < n:
        hole.append(lt[idx])
        hcnt += 1
    else:
        hole[findmin(idx)] = val
        count += 1
print(count)