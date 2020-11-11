t = int(input())
x = 1
y = 1


for i in range(t):
    w, h, a = map(int, input().split())
    while y > 0:
        y = a % (h - w)
        x += 1
        if y < h - w:
            break

    print(y * 100 + x)
    if x != 1:
        print()