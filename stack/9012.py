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
                print("NO")
        if a_count == b_count:
            print("YES")
        else:
            print("NO")
"""

N = int(input())

for _ in range(N):
    arr = str(input())
    count = 0
    for i in arr:
        if i=="(":
            count +=1
        elif i == ")":
            count -=1
        if count <0:
            break
    if count ==0:
        print("YES")
    else:
        print("NO")
        """