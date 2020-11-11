import math

a, b, h = map(int, input().split())

n = math.ceil((h-a)/(a-b))+1
print(n)