n= int(input())

result=[]

for i in range(0, n+1):
    if i ==0 :
        result.append(i)
    elif i== 1:
        result.append(i)
    else:
        result.append(result[i-2]+result[i-1])

print(result[n])