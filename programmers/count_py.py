def solution(s):
    answer = True
    count_y = s.count('y') + s.count("Y")
    count_p = s.count("p") + s.count("P") 
    if count_y == count_p:
        return True
    else:
        return False