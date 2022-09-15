def DFS1():
    cnt=3
    print(cnt)

def DFS2():
    #global cnt _ 전역변수 cnt사용
    if cnt==5:
        cnt=cnt+1
        print(cnt)

        
if __name__=="__main__":
    cnt=5
    DFS1()
    DFS2()
    print(cnt)

