prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = [0]* len(prices)
    for i in range(len(prices)):
        second = 0
        for j in range(i+1, len(prices)):
            if prices[i] <=  prices[j]:
                second += 1
            else:
                second += 1
                break
        answer[i] = second
    return answer



solution(prices)
