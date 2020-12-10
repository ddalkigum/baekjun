import math

progress = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progress, speeds):
    days = []
    answer =[]
    for i in range(len(progress)):
        days.append(math.ceil((100-progress[i])/ speeds[i]))
        
    for day in range(len(days)):
        count =1
        if days[day]== 0:
            pass
        else:
            for day_2 in range(1, len(days)):
                if day < day_2:
                    if days[day] >= days[day_2]:
                        count += 1
                        days[day_2] =0     
                    else:
                        break           
            answer.append(count)
    print(answer)

solution(progress, speeds)
        
        
    