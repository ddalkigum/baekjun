import sys

N = int(sys.stdin.readline())
arr = [0] * N

for r in range(N):
    i, j = map(int, sys.stdin.readline().split())
    arr[r] = [i, j]
arr = sorted(arr)

for k in arr:
    print(k[0], k[1])
