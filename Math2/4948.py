def prime_number(number):
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


arr = []

for k in range(2, 123456 * 2):
    if prime_number(k):
        arr.append(k)

num = int(input())

while num != 0:
    count = 0
    for j in arr:
        if j > num and j <= 2 * num:
            count += 1
    print(count)
    num = int(input())
