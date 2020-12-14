land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]	

def solution(land):
    from collections import deque
    answer = 0
    deq_first = deque(land[0])
    deq_second = deque(land[1])
    deq_third = deque(land[2])
    for i in range(4):
            for j in range(4):
                if i != j:
                    for k in range(4):
                        if j != k:

    return answer

solution(land)