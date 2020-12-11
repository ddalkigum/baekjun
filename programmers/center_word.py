s = "abcde"
import re
def solution(s):
    answer=""
    for word in range(int(len(s)/2)+1):
        if len(s)%2 ==0:
            if word == int(len(s)/2):
                answer = (s[word-1]+ s[word])
        else:
            if word == int(len(s)/2):
                answer = (s[word])
    return answer
solution(s)