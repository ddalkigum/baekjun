M = int(input())
N = int(input())
prime = []

for i in range(M, N + 1):
    count = 0
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1
            if count > 2:
                break
    if count == 1:
        prime.append(i)
if len(prime) != 0:
    print(sum(prime))
    print(prime[0])
else:
    print("-1")
