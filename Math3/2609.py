n,m = list(map(int, input().split()))
b=0

for i in range(m, 0, -1):
    if m%i == 0 and n%i ==0:
        b =i
        break
a = m*n / b

print(b)
print(int(a))