def solution(participant, completion):
    answer =""
    participant.sort()
    completion.sort()

    if len(completion) == 0:
        answer = ""
    else:
        for i in range(len(participant)-1):
            if participant[i] != completion[i]:
                answer = participant[i]
                break
            else:
                answer = participant[-1] 
    return answer