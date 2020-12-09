N = int(input())
arr = list(map(int, input().split()))
a = 0

for i in range(len(arr)):
    if i == 0:
        pass
    else:
        for j in range(arr[i], 0, -1):
            if arr[0]%j ==0 and arr[i]%j ==0:
                a = j
                top = int(arr[0]//a)
                bottom = int(arr[i]//a)
                print("%d/%d" % (top,bottom))
                break;