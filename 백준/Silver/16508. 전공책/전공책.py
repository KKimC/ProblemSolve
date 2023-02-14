import sys
in_str = input()
bcnt = int(input())
price = []
in_major = []
for i in range(bcnt):
    p, m = input().split()
    price.append(int(p))
    in_major.append(m)

def wordinbook(word, book, price):
    cnt = 0
    for w in word:
        if w in book:
            cnt += 1
            book = book.replace(w, ' ', 1)
            if cnt == len(word):
                return price
    return sys.maxsize

result = []

for i in range(1 << len(in_major)):
    search_str = ""
    sum_price = 0
    for j in range(len(in_major)):
        if (i & 1 << j) != 0: #
            search_str += in_major[j]
            sum_price += price[j]

    result.append(wordinbook(in_str, search_str, sum_price))

result = min(result)
if result == sys.maxsize:
    result = -1

print(result)