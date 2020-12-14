n = 4

def solution(n):
    answer = []
    plate = [[0] * n] *n
    print(plate)
    print(plate[0][0])
    print(plate[0])
    for i in range(1, n+1):
        plate[i-1][0] = i
    print(plate)
    
    return answer

solution(n)