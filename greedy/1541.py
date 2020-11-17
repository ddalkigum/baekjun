n = input().split("-")
arr = []
result = []

for i in n:
    if "+" in i:
        arr = i.split("+")
        result.append(int(arr[0]) + int(arr[1]))
    else:
        result.append(int(i))
value = result[0]

for j in range(1, len(result)):
    value -= result[j]
print(value)
