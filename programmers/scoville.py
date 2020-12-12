scoville = [0,0,2]
K = 2

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


solution(scoville, K)