N = int(input())

for _ in range(N):
    jo_x, ba_x, j_r, jo_y, ba_y, b_r = map(int, input().split())

    between = ((ba_y - jo_y) ** 2 + (ba_x - jo_x) ** 2) ** 0.5

    if between == 0 and j_r == b_r:
        print(-1)
    elif between == (b_r + j_r) or between == abs(j_r - b_r):
        print(1)
    elif abs(j_r - b_r) < between < (j_r + b_r):
        print(2)
    else:
        print(0)