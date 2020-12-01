N = int(input())

if N < 100:
    value = N
else:
    value = 99
    for i in range(100, N + 1):
        num = str(i)
        value_one = int(num[2]) - int(num[1])
        value_two = int(num[1]) - int(num[0])
        if value_one == value_two:
            value += 1
print(value)
