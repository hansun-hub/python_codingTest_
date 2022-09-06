h,m = map(int,input().split())
oven = int(input())

if m+oven<60:
    print(h,m+oven)
else:
    if h==23:
        print(0+((m+oven)/60)-1,(m+oven)%60)

    else:
        print(((m+oven)/60)-1,(m+oven)%60)
        h=23
