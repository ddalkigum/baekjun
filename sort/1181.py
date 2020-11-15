import sys

N = int(sys.stdin.readline())
arr = [0] * N
num = []


for r in range(N):
    word = sys.stdin.readline()
    arr[r] = word
arr = set(arr)

for i in arr:
    num.append((len(i), i))
num.sort()
for j in num:
    print(j[1].strip("\n"))
