N, M = map(int, input().split())
arr = []
a = 1

for _ in range(M):
    arr.append(a)

while arr[0] <= N:
    arr[1] = 1
    while arr[1] <= N:
        print(arr)
        arr[1] += 1
    arr[0] += 1
