'''
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
'''

N= int(input())
a_list=[]



for _ in range(N):
    a= list(map(str, input()))
    a_list.append(a)

for i in range(0, len(a_list)):
    result=[]
    s=0
    for j in range(0, len(a_list[i])):
        if a_list[i][j] == "O":
            s+= 1        
            if a_list[i][j]:
                result.append(s)
        else:
            s=0
            
            
    print(sum(result))

