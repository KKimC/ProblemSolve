n, d, k, c = map(int, input().split())
arr = []
l, r = 0, k-1
result = -987654321
hashTable = dict()
hashTable[c] = 1
for _ in range(n):
    arr.append(int(input()))
for i in range(r + 1):
    if arr[i] not in hashTable:hashTable[arr[i]] = 0
    hashTable[arr[i]] += 1
for _ in range(n):
    hashKey = arr[l]
    result = max(len(hashTable), result)
    if hashKey not in hashTable:hashTable[hashKey] = 0
    hashTable[hashKey] -= 1
    if hashTable[hashKey] == 0: del hashTable[hashKey]
    l += 1; r += 1
    if r >= n:
        r -= n
    if arr[r] not in hashTable:hashTable[arr[r]] = 0
    hashTable[arr[r]] += 1
print(result)