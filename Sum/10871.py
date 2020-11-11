a, b = map(int, input().split())
c = list(map(int, input().split()))

for i in c:
    if b > i:
        print(i)