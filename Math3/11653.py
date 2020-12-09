N = int(input())

while N != 1:
    for i in range(2, N + 1):
        if (N % i) == 0:
            print(i)
            N = N // i
            break

"""

import sys

N = int(sys.stdin.readline())
ROOT = int(N ** 0.5)
i=2

while N:
    if i>ROOT: break

    if N%i == 0:
        print(i)
        N = N//i
    else:
        i+=1

if N > 1: print(N)

"""