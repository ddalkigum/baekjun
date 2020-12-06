N, M = map(int, input().split())
arr = [0] * M


def backtracking(index, n, m):
    if index == m:
        for i in arr:
            print(i, end=" ")
        print()
    else:
        for j in range(1, N + 1):
            arr.append(j)
            backtracking(index + 1, n, m)


backtracking(1, N, M)