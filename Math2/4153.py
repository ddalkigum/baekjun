a, b, c = map(int, input().split())

while a != 0 or b != 0 or c != 0:
    arr = list([a, b, c])
    max_number = max(arr)
    arr.remove(max_number)

    if max_number ** 2 == arr[0] ** 2 + arr[1] ** 2:
        print("right")
    else:
        print("wrong")
    a, b, c = map(int, input().split())
