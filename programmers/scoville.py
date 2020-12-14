
scoville = [0,0,2]
K = 2
"""
def solution(scoville, K):
    answer = 0
    sum_scoville = scoville[0]
    scoville.sort()
    for i in range(len(scoville)):
        try:
            sum_scoville = sum_scoville + scoville[i+1]*2
            if sum_scoville >= K :
                answer += 1
                print(answer)
                return answer
            else:
                answer += 1
        except IndexError:
            return -1
"""

def solution(scv, K):
    import heapq 
    answer = 0
    h = [] 
    for i in scv: 
        heapq.heappush(h,i) 
    while h[0] < K: 
        try:
            heapq.heappush(h,heapq.heappop(h)+(heapq.heappop(h)*2)) 
        except IndexError:
            return -1 
        answer += 1
    return answer
