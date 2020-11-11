N= int(input())

a=[]
s=[]

for i in range(0,N):
    a.append(list(input()))

for j in range(len(a)-1):
    if j < len(a)-1:
        for k in range(len(a[j])):
            if a[j][k] == a[j+1][k]:
                if a[j+1][k]==a[j+2][k]:
                    s.append(a[j][k])
                    print(s)
                else:
                    s.append("?")
                    print(s)

print(s)