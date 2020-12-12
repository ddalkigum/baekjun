skill = "CBD"
skill_trees = ['CBADF', 'AECB', 'AQWER', 'BDA']	



def solution(skill, skill_trees):
    from collections import deque
    answer = 0
    while skill_trees:
        learned = True
        deq = deque(list(skill))
        learn=[]
        skill_tree = skill_trees.pop()
        for i in skill_tree:
            if i in skill:
                learn.append(i)
        for j in range(len(learn)):
            if learn[j] != skill[j]:
                learned = False
                break
        if learned == True:
            answer += 1
    return answer

solution(skill, skill_trees)