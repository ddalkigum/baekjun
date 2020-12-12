s ="aabbaccc"

def solution(s):
    from collections import deque
    answer = 0
    que = deque(s)
    print(que)
    while que:
        words = []
        word = ""
        print(que)
        word = que.popleft()
        words += word
    print(words)

    return answer

solution(s)