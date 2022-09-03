h,m = map(int,input().split())

if m<44:
    tmp=45-m
    m=60-tmp
    if(h==0):
        h=23
    else:
        h=h-1
else:
    m=-45

print(h,m)