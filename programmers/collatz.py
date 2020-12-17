num = 6

def solution(num):
    answer = 0
    count =0
    while num != 1:
        if count == 501:
            return -1
        else:
            if num % 2 == 0:
                num = num / 2
            elif num % 2 != 0:
                num = num * 3 + 1
        count += 1 
    return count

solution(num)