N = int(input())
result = 0

for i in range(1, N):
    con = list(map(int, str(i)))
    sum_number = i + sum(con)
    if sum_number == N:
        result = i
        break
print(result)
