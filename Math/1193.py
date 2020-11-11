x= int(input())
n= 1

while x>0:
    x -=n
    n +=1

num = x+n-1
if n %2 ==0:
    print(n-num,"/",num, sep="")
else:
    print(num,"/",n-num, sep="")
