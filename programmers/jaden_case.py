s =  "A  Sdf Fft "

def solution(s):
    answer = ''
    count = 1
    for i in s:
        if i == " ":
            count = 1
            answer += " "
        elif count == 1 :
            answer += i.upper()
            count =0
        else:
            answer += i.lower()
    print(answer)
    return answer

solution(s)