"""
a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)


for i in range(10):
    print(mul.count(str(i)))
"""
"""
arr = [0] * 10
num_arr = []

for i in range(10):
    arr[i] = int(input())

for j in arr:
    num_arr.append(j % 42)

num_arr = set(num_arr)
print(len(num_arr))
"""
"""
N = int(input())
M = [0] * N
M = list(map(int, input().split()))
value_arr = []
max_value = max(M)

for i in M:
    num = i / max_value * 100
    value_arr.append(num)
score = sum(value_arr) / len(value_arr)
print(score)
"""


self_number = []
co_num = []

numarr = list(range(1, 10001))

for i in numarr:
    num = int(i)
    for j in i:
        num += int(j)
    self_number.append(num)
(set(self_number))
for k in range(10000):
    if k in self_number:
        pass
    else:
        co_num.append(k)
for s in co_num:
    print(s)

    """ 
    def selfnum(num):
    ret = num
    while(num!=0):
        ret += num % 10
        num = int(num / 10)
    return ret

li = list(range(10001))

for i in range(1,10001):
    tmp = selfnum(i)
    if tmp <= 10000: li[tmp] = 0

for i in li:
    if i != 0: print(i)
    """
