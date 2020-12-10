n=5
lost =[2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    arr = [1]*n
    for i in lost:
        arr[i-1] = 0
    for j in range(n):
        if j ==0: 
            if j in reserve:
                arr[j+1] =1
        elif j == n-1:
            if j in reserve:
                arr[j-1] =1
        else:
            if arr[j] == 0:
                pass
            else:
                if arr[j-1] == 0:
                    if arr[j] in reserve:
                        arr[j-1] = 1
                elif arr[j+1] ==0:
                    if arr[j] in reserve:
                        arr[j+1] = 1
    print(arr)
    answer = 0
    return answer
solution(n, lost, reserve)