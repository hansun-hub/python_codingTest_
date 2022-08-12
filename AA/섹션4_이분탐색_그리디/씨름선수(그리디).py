import sys
sys.stdin=open("input.txt","rt")

n=int(input())
body = []
for i in range(n):
    a,b = map(int, input().split())
    body.append((a,b))
body.sort(reverse=true)
largest=0
for x,y in body:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)

