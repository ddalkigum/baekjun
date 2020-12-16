def solution(s):
    from collections import deque
    answer = ''
    count = 0
    deq = deque(list(s))
    while deq:
        word = deq.popleft()
        if word == " ":
            count = 1
        if count % 2 == 0:
            answer += word.upper()
            count += 1
        else:
            answer += word.lower()
            count += 1
    return answer