import sys

N = int(input())
arr = [0] * N

for r in range(len(arr)):
    i, j = map(str, sys.stdin.readline().split())
    arr[r] = [i, j]
arr.sort(key=lambda x: int(x[0]))
for age, name in arr:
    print(age, name)
