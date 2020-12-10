numbers= [5,0,2,7]

def solution(numbers):
    arr =[]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i > j :
                if numbers[i]+numbers[j] in arr:
                    pass
                else:
                    arr.append(numbers[i]+numbers[j])
    answer = sorted(arr)
    print(answer)
    return answer

solution(numbers)

# result = [2,3,4,5,6,7]