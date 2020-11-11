N = int(input())
arr = []
result = []


for i in range(N):
    h, w = list(map(int, input().split()))
    arr.insert(i, [h, w])

for i in range(len(arr)):
    rank = len(arr)
    for j in range(len(arr)):
        if arr[i][0] > arr[j][0] or arr[i][1] > arr[j][1]:
            rank -= 1
    result.append(rank)

for k in range(len(result)):
    print(result[k], end=" ")