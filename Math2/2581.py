M, N = map(int, input().split())
arr = []


def prime_list(n):
    sieve = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i] == True]


prime = prime_list(N)

for i in prime:
    if i < M:
        arr.append(i)

del prime[: len(arr)]

if arr == None:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])