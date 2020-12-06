N, M = map(int, input().split())

arr = [0] * (M + 1)


def backtracking(index, n, m):
    if index == m:
        for i in arr:
            print(i, end=" ")
    else:
        for j in range(1, n + 1):
            arr[index] = j
            backtracking(
                index + 1, n, m
            )  # 이 부분에서 재귀를 하게 되면 index값이 계속해서 1씩 더해졍야 하는거 아닌가? 어떻게 1, 2씩 왔다갔다 하지


backtracking(0, N, M)
