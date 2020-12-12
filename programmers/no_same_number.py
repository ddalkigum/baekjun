arr = [1, 1]	

def solution(arr):
    from collections import deque
    answer = []
    lists = []
    deq = deque(arr)
    while deq:
        number = deq.popleft()
        if len(deq) ==0:
            if len(answer) == 0:
                answer.append(number)
            elif answer[-1] == number:
                pass  
            else:
                answer.append(number)
        elif deq[0] == number:
            pass
        else:
            answer.append(number)
    return answer


solution(arr)