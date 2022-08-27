import sys
from collections import deque
sys.stdin = open("input.txt","r")
n,k = map(int, input().split())
dq = list(range(1,n+1)) #1부터 8까지 리스트 생성_ 아직은 리스트
dq = deque(dq)
while dq: #큐가 비면은 멈춤 
    for _ in range(k-1): #하나의 패턴이다
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft() #비어버린다.
