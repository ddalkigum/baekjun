phone_number = "01033334444"

def solution(phone_number):
    from collections import deque
    answer = ''
    deq = deque(list(phone_number))
    while deq:
        number = deq.popleft()
        if len(deq) <4:
            answer += number
        else:
            answer += "*"
    return answer

solution(phone_number)