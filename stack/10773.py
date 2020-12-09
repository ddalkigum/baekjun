N = int(input())
arr=[]

for i in range(N):
    number = int(input())
    if number != 0:
        arr.append(number)
    else:
        del arr[-1]
print(sum(arr))