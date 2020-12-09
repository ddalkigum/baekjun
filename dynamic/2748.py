import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N + 1):
    arr.append(i)

for i in range(2, N + 1):
    arr[i] = arr[i - 1] + arr[i - 2]

print(arr[-1])

# 이 문제 이해안됨

"""
N = int(input())
count = []


def dynamic(n):
    if n % 3 == 0:
        n = n / 3
        count.append("1")
        if n == 1:
            print(len(count))
        else:
            dynamic(n)
    elif n % 2 == 0:
        n = n / 2
        count.append("1")
        if n == 1:
            print(len(count))
        else:
            dynamic(n)
    else:
        n -= 1
        count.append("1")
        if n == 1:
            print(len(count))
        else:
            dynamic(n)
"""