N = int(input())

for _ in range(N):
    a_count = 0
    b_count = 0
    arr =str(input())
    if arr[-1] =="(":
        print("NO")
    elif arr[0] ==")":
        print("NO")
    else:
        for i in arr:
            if i == "(":
                a_count += 1
            elif i == ")":
                b_count += 1
            if a_count < b_count:
                break
        if a_count == b_count:
            print("YES")
        else:
            print("NO")
