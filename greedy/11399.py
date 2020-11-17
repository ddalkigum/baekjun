from math import floor

N = int(input())
p = list(map(int, input().split()))
sum = 0

for i in range(1, N + 1):
    m = sorted(p)
    sum += floor(m[i - 1]) * floor(N - (i - 1))
print(sum)