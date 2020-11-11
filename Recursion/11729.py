def hanoi(n, a, b, c):
    if n < 2:
        print(a, b)
        return
    hanoi(n - 1, a, b, c)
    print(a, c)
    hanoi(n - 1, c, a, b)


n = int(input())

print((2 ** n) - 1)
hanoi(n, 1, 3, 2)