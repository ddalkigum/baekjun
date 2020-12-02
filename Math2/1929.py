import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(range(N, M + 1))


def prime_number(a):
    if a == 1:
        return False
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True


for i in arr:
    if prime_number(i):
        sys.stdout.write(str(i) + "\n")
