from collections import deque



for i in range(int(input())):
    left_q = deque([])
    right_q = deque([])
    for s in input():
        if s == "<":
            if left_q:
                right_q.appendleft(left_q.pop())
        elif s == ">":
            if right_q:
                left_q.append(right_q.popleft())
        elif s == "-":
            if left_q:
                left_q.pop()
        else:
            left_q.append(s)
    print("".join(left_q+right_q))