def solution(n, m):
    from math import gcd
    answer = [0]*2
    gcd_number = ged(n, m)
    lcm = (n*m)/gcd_number
    answer[0] = gcd_number
    answer[1] = lcm
    return answer