import sys
sys.stdin = open("input.txt","r")
n=int(input()) #시험장의 개수 
arr=list(map(int,input().split())) #응시자의 수 
b,c = map(int,input().split()) #총감독관이 감시할 수 있는 수 : B, 부감독관이 감시할 수 있는 수 : C

anwer = len(arr) #무조건 한 명의 총감독관이 있어야 함

for i in arr:
    if i-b > 0:
        if (i-b)%c==0:
            answer+=(i-b)//c
        else:
            answer+=((i-b)//c+1)
print(answer)           
