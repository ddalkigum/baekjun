import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N + 1):
    arr.append(i)

for i in range(2, N + 1):
    arr[i] = arr[i - 1] + arr[i - 2]

print(arr[-1])