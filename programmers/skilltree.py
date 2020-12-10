skill = "CBD"
skill_trees = ["C"]

def solution(skill, skill_trees):
    answer = 0
    
    for i in range(len(skill_trees)):
        count = 0 
        arr = []
        for j in range(len(skill)):
            skill_order = 0
            for k in range(len(skill_trees[i])):
                if skill[j] not in skill_trees[i]:   
                    pass
                else:
                    skill_order += 1
                    if skill[j] == skill_trees[i][k]:
                        break 
            arr.append(skill_order)
        for m in arr:
            for n in range(1, len(arr)):
                if m == arr[n] :
                    break
                elif m < arr[n]:
                    count +1
        if count >0:
            answer+=1
    print(answer)
    return answer

solution(skill, skill_trees)