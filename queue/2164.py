
N = int(input())
arr=[]

for i in range(1, N+1):
    arr.append(i)

def shuffle(card):   
    answer=[]
    if len(card) ==1:
        print(card[0]) 
    else:
        for i in range(len(card)):
            if i %2 == 0:
                card[i] = 0
        for j in card:
            if j !=0:
                answer.append(j)    
        if len(answer)==1:
            print(answer[0])
        else:
            shuffle(answer)
    
    
shuffle(arr)
        


