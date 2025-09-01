# Qual será a saída do seguinte trecho de código?

d = {}
d[1] = 1
d['1'] = 2
d[1] += 1

print(d)
sum = 0

for k in d:
    sum += d[k]
print(sum)
