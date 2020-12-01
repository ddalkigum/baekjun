a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)


for i in range(10):
    print(mul.count(str(i)))