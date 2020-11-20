import sys

n = int(sys.stdin.readline())
arr = [1, 1, 1, 2, 2, 3]

for _ in range(n):
    m = int(sys.stdin.readline())
    length = len(arr)
    if m > length:
        for l in range(length, m + 1):
            arr.append(arr[l - 1] + arr[l - 5])
    sys.stdout.write((str(arr[m - 1]) + "\n"))
