def solution(seoul):
    answer = ''
    answer = [x for x in range(len(seoul)) if seoul[x] == "Kim"]
    return f"김서방은 {answer[0]}에 있다"