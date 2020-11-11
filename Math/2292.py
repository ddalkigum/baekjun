x = int(input())
n = 1
i = 0
while x > 0:

    x = x - n
    n = 6 * (2 ** i)
    i += 1

print(i)


x = int(input())
n = 1
i = 1
while x > n:
    n += 6 * i
    i += 1
print(i)