N, M = map(int, input().split())
arr = [0] * M


def backtracking(index, n, m):
    if index == m:
        for i in arr:
            print(i, end=" ")
        print()
    else:
        for j in range(1, n + 1):
            if j > 1 or j == n - 1:
                if arr[j] >= arr[j - 1]:
                    arr[index] = j
                    backtracking(index + 1, n, m)


backtracking(0, N, M)
