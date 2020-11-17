from itertools import permutations

N, M = map(int, input().split())
arr = [0] * N

if N < 8 and M < 8:
    for i in range(N):
        arr[i] = i + 1
    lists = permutations(arr, M)
    for j in lists:
        print(j)