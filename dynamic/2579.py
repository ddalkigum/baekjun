N = int(input())
arr = []
sum_num = [0] * N
count = 0

for _ in range(N):
    arr.append(int(input()))

for j in range(len(arr)):
    if j == 0:
        sum_num[j] = arr[0]
    elif j == 1:
        sum_num[j] = arr[0] + arr[j]
    elif j == 2:
        sum_num[j] = max(arr[0] + arr[2], arr[1] + arr[2])
    else:
        sum_num[j] = max(arr[j] + sum_num[j - 2], arr[j] + arr[j - 1] + sum_num[j - 3])
print(sum_num[N - 1])