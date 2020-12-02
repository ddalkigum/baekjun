arr = []
x_list = []
y_list = []

for _ in range(3):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)):
    x_list.append(arr[i][0])
    y_list.append(arr[i][1])

for j in x_list:
    if x_list.count(j) == 1:
        x = j
for k in y_list:
    if y_list.count(k) == 1:
        y = k

print(x, y)
