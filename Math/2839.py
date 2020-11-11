n = int(input())
x = 0

while True:
    if n % 5 == 0:
        x = x + (n // 5)
        print(x)
        break
    n = n - 3
    x = x + 1
    if n < 0:
        print(-1)
        break
