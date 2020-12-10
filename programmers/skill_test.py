import re
n = int(input())

def solution(n):
    answer = ""
    word =""
    for i in range(n):
        if i%2 == 0:
            word+="수"
        else:
            word+="박"
    answer = f'"{word}"'
    print(answer)
    return answer

solution(n)