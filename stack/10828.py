import sys

N = int(sys.stdin.readline())
arr= []

for _ in range(N):
    word = input()
    if "push" in word:
        word = word[4:]
        arr.append(int(word))
    elif word =="pop":
        if len(arr)==0:
            print(-1)
        else:
            print(arr[-1])
            del arr[-1]
    elif word =="size":
        print(len(arr))
    elif word =="empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif word =="top":
        if len(arr) == 0:
            print(-1)
        else:    
            print(arr[-1])
        
            