sN= int(input())
a_list=[]
b_list=[]
for i in range(N):
    a= int(input())
    b=int(input())
    a_list.append(a)
    b_list.append(b)

result= 0

for i in range(N):
    result+= a_list.pop(a_list.index(min(a_list)))*b_list.pop(b_list.index(max(b_list)))
    
print(result)