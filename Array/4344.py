C= int(input())
point=[]

for i in range(C):
    N= list(map(int, input().split()))
    point.append(N)

for j in range(len(point)):
    
    avg_list= []
    avg = sum(point[j][1:])/(len(point[j])-1)
    
    for p in range(len(point[j])):
        if p >= 1:
            if point[j][p] > avg:
                avg_list.append(point[j][p])
    average= float(len(avg_list)/(len(point[j])-1))
    print("%.3f%%" % (average*100))
                
                
