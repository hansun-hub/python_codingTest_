import sys
sys.stdin=open("input.txt","rt")
n,limit = map(int, input().split())
p=list(map(int,input().split()))
p.sort()
cnt=0
while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.pop(0)
        p.pop()
        cnt+=1
print(cnt)
