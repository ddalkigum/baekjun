N = int(input())
a = []

for _ in range(N):
    a.append(int(input()))

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

for k in a:
    print(k)
