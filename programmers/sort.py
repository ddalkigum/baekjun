strings =["sun", 'bed', 'car']
n = 1

def solution(strings, n):
    answer = [0]*len(strings)
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()
    for j in range(len(answer)):
        answer[j] = strings[j][1:]
    return answer

solution(strings, n)