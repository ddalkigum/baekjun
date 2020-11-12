n = int(input())
arr = list(map(int, input().split()))
count = 0

for i in range(n):
    if arr[i] == 1:
        continue
    elif arr[i] == 2:
        count += 1
    elif arr[i] % 2 == 0:
        pass
    else:
        for j in range(2, arr[i] + 1):
            if arr[i] % j == 0:
                if arr[i] == j:
                    count += 1
print(count)
