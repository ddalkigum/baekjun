a =5
b =24

def solution(a, b):
    from datetime import date
    answer = date(2016,a,b).strftime('%a').upper()
    return answer

solution(a, b)