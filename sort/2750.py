a = list(map(int, input().split()))
for i in a:
    for j in a:
        if a[i] == a[j]:
            a.remove(j)
            