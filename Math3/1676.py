N = int(input())
fac = 1
count = 0

for i in range(1, N+1):
    fac *= i       
fac = str(fac)
for j in range(len(fac), 0, -1):
    if fac[j-1] == "0":
        count +=1
    else:
        break

print(count)