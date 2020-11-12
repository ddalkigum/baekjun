t = int(input())

for i in range(t):
    h, w, o = map(int, input().split())
    floor = o % h
    room_number = o // h + 1
    if o % h == 0:
        floor = h
        room_number = o // h

    print(floor * 100 + room_number)
