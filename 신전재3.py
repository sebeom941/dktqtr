a = int(input("나이를 입력하세요: "))
d = str(input("성별을 입력하세요 (남자, 여자, 트랜스젠더): "))

if a > 19:
    if d == '남자':
        print('성인남자')
    elif d == '여자':
        print('성인여자')
    elif d == '트랜스젠더':
        print('성인트랜스젠더')
else:
    if d == '남자':
        print('소년')
    elif d == '여자':
        print('소녀')
    elif d == '트랜스젠더':
        print('청소년트랜스젠더')