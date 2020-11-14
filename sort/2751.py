import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))


for j in sorted(arr):
    sys.stdout.write(str(j) + "\n")
