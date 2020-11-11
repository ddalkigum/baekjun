n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

# count_a -> 첫 보드가 B일 경우
# count_b -> 첫 보드가 W일 경우
for i in range(n - 7):
    for j in range(m - 7):
        count_a = 0
        count_b = 0
        for k in range(i, i + 8):
            for h in range(j, j + 8):
                if k % 2 == 0 and h % 2 == 0:
                    if board[k][h] == "W":
                        count_a += 1
                elif k % 2 == 1 and h % 2 == 1:
                    if board[k][h] == "W":
                        count_a += 1
                elif k % 2 == 0 and h % 2 == 1:
                    if board[k][h] == "B":
                        count_a += 1
                elif k % 2 == 1 and h % 2 == 0:
                    if board[k][h] == "B":
                        count_a += 1
        for k in range(i, i + 8):
            for h in range(j, j + 8):
                if k % 2 == 0 and h % 2 == 0:
                    if board[k][h] == "B":
                        count_b += 1
                elif k % 2 == 1 and h % 2 == 1:
                    if board[k][h] == "B":
                        count_b += 1
                elif k % 2 == 0 and h % 2 == 1:
                    if board[k][h] == "W":
                        count_b += 1
                elif k % 2 == 1 and h % 2 == 0:
                    if board[k][h] == "W":
                        count_b += 1

        min_value = min(count_a, count_b)
print(min_value)
