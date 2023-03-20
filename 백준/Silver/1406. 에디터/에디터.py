from collections import deque

left_q = deque(list(input()))
right_q = deque([])

for i in range(int(input())):
    order = input().split()
    if order[0] == "L":
        if left_q:
            right_q.appendleft(left_q.pop())
    if order[0] == "D":
        if right_q:
            left_q.append(right_q.popleft())
    if order[0] == "B":
        if left_q:
            left_q.pop()
    if order[0] == "P":
        left_q.append(order[1])
print("".join(left_q+right_q))
