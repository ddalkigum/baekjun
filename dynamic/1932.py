N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    if i == 0:
        continue
    elif i == 1:
        arr[i][0] = arr[0][0] + arr[i][0]
        arr[1][1] = arr[0][0] + arr[i][1]
    else:
        for j in range(len(arr[i])):
            if j == 0:
                arr[i][j] = arr[i - 1][j] + arr[i][j]
            elif i == j:
                arr[i][j] = arr[i - 1][j - 1] + arr[i][j]
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i - 1][j - 1]) + arr[i][j]
print(max(arr[N - 1]))
