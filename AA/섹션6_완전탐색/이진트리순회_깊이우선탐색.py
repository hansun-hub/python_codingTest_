def DFS(v):
    if v>7:
        return
    else:
        DFS(v*2)
        DFS(v*2+1)
        print(v,end=' ')



if __name__=="main":
    n=int(input())
    DFS(1)


