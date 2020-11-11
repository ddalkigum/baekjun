i_list= []

for i in range(9):
    i= int(input())
    i_list.append(i)

w = i_list.index(max(i_list))
i_max= max(i_list)

print(i_max)
print(w+1)