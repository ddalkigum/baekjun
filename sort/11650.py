N = int(input())
arr = [0] * N

for r in range(N):
    i, j = map(int, input().split())
    arr[r] = [i, j]
arr = sorted(arr)

for k in range(len(arr)):
    c = str(arr[k]).strip("[ , ,  ] ")
    print(c)
