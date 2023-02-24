n=int(input())
nums=sorted(list(map(int,input().split())))
answer=1
for x in range(n-1):
    for z in range(n-1,-1,-1):
            if z<x+1:break
            if nums[x]+nums[x+1]>nums[z]:
                answer=max(z-x+1,answer)
print(answer)
