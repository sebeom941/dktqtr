a,b,c=map(int,input().split())
if a+b+c==180:
    if a==b==c:
        print('정삼각형')
    elif a==b:
        print('이등변삼각형')
    elif a==c:
        print('이등변삼각형')
    elif b==c:
        print('이등변삼각형')
    else:
        print('일반 삼각형')
else:
    print('error')

