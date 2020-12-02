numarr = []
self_number = []
co_num = []

for n in range(10000):
    numarr.append(str(n))

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