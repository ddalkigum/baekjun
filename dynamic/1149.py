N = int(input())
price = []
sum_price = []
i = 1
for _ in range(N):
    price.append(list(map(int, input().split())))

while i < N:

    price[i][0] = min(price[i - 1][1], price[i - 1][2]) + price[i][0]
    price[i][1] = min(price[i - 1][2], price[i - 1][0]) + price[i][1]
    price[i][2] = min(price[i - 1][1], price[i - 1][0]) + price[i][2]

    i += 1

print(min(price[N - 1]))
