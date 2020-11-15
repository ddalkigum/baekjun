import sys

N = int(input())
arr = [0] * N

for r in range(N):
    i, j = list(map(int, sys.stdin.readline().split()))
    arr[r] = [j, i]
for k in sorted(arr):
    print(k[0], k[1])