import sys

M, N = map(int, sys.stdin.readline().split())

prime_list = []


def prime(number):
    count = 0
    for i in range(1, number):
        if number % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


for i in range(M, N + 1):
    if prime(i) == True:
        prime_list.append(i)

for j in prime_list:
    sys.stdout.write((j))
