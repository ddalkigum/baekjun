t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    dist = y - x
    count = 0
    start = 1
    num_sum = 0

    while num_sum < dist:
        count += 1
        num_sum = num_sum + start
        if count % 2 == 0:
            start += 1
    print(count)
