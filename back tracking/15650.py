import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split(" "))
li = []
for i in range(1, N + 1):
    li.append(i)

for each in list(combinations(li, M)):
    for num in each:
        print(num, end=" ")
    print()