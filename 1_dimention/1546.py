N = int(input())
M = [0] * N
M = list(map(int, input().split()))
value_arr = []
max_value = max(M)

for i in M:
    num = i / max_value * 100
    value_arr.append(num)
score = sum(value_arr) / len(value_arr)
print(score)