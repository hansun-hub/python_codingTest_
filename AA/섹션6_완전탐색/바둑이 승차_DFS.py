from collections import deque
def DFS(L,sum):
    global result
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)



if __name__=="__main__":
    c,n=map(int,input().split())
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
    DFS(0,0)
    print(result)
