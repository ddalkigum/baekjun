from itertools import combinations

arr = ["A", "B", "C", "D", "E", "F"]
lists = list(combinations(arr, 3))

for i in lists:
    print(i)
    if "A" in i and "F" in i:
        print("AF")
        lists.remove(i)
    elif "B" in i and "E" in i:
        print("BE")
        lists.remove(i)
        print(lists)
    elif "C" in i and "D" in i:
        print("CD")
        lists.remove(i)
    else:
        print("ok")