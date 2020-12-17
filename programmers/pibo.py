def solution(n):
    answer = 0
    pibo =[0]*100001
    for i in range(1, n+1):
        if i == 1:
            pibo[i] = 1
        elif i == 2:
            pibo[i] =1
        else:
            pibo[i] = pibo[i-2] + pibo[i-1]
            answer = pibo[i] % 1234567
    return answer