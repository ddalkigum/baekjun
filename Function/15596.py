a, b, c, = list(map(int, input().split()))
bp= 0


if a/(b-c) <0:
    bp=-1
else:
    bp= a/(b-c) +1
print(bp)
