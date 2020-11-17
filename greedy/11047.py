N, K = map(int, input().split())
arr = []
count = 0

for _ in range(N):
    arr.append(int(input()))


for i in range(1, len(arr) + 1):
    if K - arr[-i] >= 0:
        mul = K // arr[-i]
        K = K - mul * arr[-i]
        count += mul * 1
        if K == 0:
            break
print(count)
