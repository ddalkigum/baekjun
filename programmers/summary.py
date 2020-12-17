nums = [1, 2, 3, 4]

def solution(nums):
    from itertools import combinations
    answer = 0
    count = 0
    sum_numbers = combinations(nums, 3)
    numbers = []
    for i in (sum_numbers):
        numbers.append(sum(i))
    for j in range(1, len(max(int(numbers**0.05)))):
        if int(numbers[j]**0.05) % j == 0:
            break
        if int(numbers[j]**0.05) == j:
            answer += 1
    print(answer)
    return answer

solution(nums)