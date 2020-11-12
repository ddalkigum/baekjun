n = int(input())
m = n
cycle = 0

while True:
    a = n // 10
    b = n % 10
    sum_num = a + b
    cycle += 1
    n = int(str(b) + str(sum_num % 10))
    if n == m:
        break
print(cycle)
