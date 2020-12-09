N = int(input())
arr = [0]*N
answer = []
q = []



for i in range(N):
    arr[i] = int(input())
min_value = min(arr)

for j in range((min_value),1, -1):
    for k in arr:
        a=k%j      
        answer.append(a)
    if len(set(answer))==1:
        q.append(j)
        answer = []
    answer = []
for l in sorted(q):
    print(l, end=" ")

