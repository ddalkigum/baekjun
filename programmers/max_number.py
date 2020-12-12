numbers = [21, 212]

def solution(numbers):
    from  itertools import permutations
    answer = ''
    sum_numbers = []
    p =permutations(numbers)
    for i in p:
        sum_number = ""
        for j in i:
            sum_number += str(j)
        sum_numbers.append(sum_number) 
    answer = max(sum_numbers)
    return answer

solution(numbers)
