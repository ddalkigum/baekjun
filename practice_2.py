plate = [[0]*19 for i in range(19)]

a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    plate[b-1][c-1] = 1

for j in range(len(plate)):
    for k in range(len(plate)):
        print(plate[j][k], end=" ")
    print()
