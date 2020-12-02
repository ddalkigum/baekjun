arr = [0] * 10
num_arr = []

for i in range(10):
    arr[i] = int(input())

for j in arr:
    num_arr.append(j % 42)

num_arr = set(num_arr)
print(len(num_arr))