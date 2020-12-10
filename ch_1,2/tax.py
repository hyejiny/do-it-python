def service_price(a):
    if a == 'A':
        result = 23 * 1.1
    if a == 'B':
        result = 40 * 1.1
    else:
        result = 67 * 1.1

    re = round(result,1)

    return re


service = input('서비스 종류를 입력하세요.(A/B/C)')
value_t = input('부가세를 포함하나요?(y/n)')

if value_t == 'y':
    print('{}만원입니다.'.format(service_price(service)))