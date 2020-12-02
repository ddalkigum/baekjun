x, y, w, h = map(int, input().split())

value_arr = [h - y, w - x, y - 0, x - 0]
print(min(value_arr))