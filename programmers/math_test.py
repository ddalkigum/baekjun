answers = [1,2,3,4,5]

def solution(answers):
    answer = []
    a_answer = [1,2,3,4,5]
    b_answer = [2,1,2,3,2,4,2,5]
    c_answer = [3,3,1,1,2,2,4,4,5,5]
    a_count = 0
    b_count = 0
    c_count = 0
    for i in range(len(answers)):
        if answers[i] == a_answer[i%len(a_answer)]:
            a_count += 1
        if answers[i] == b_answer[i%len(b_answer)]:
            b_count += 1
        if answers[i] == c_answer[i%len(c_answer)]:
            c_count += 1
    max_number = max(a_count, b_count, c_count)
    if max_number == a_count:
        answer.append(1)
    if max_number == b_count:
        answer.append(2)
    if max_number == c_count:
        answer.append(3)
    return answer

solution(answers)