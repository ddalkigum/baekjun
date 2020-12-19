s = "Zbcdefg"

def solution(s):
    answer = ''
    sort_s = sorted(s, reverse=True)
    for i in sort_s:
        answer += i
    return answer

solution(s)