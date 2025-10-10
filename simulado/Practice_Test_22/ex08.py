# Qual será a saída do seguinte trecho de código?

d = {} # add dicionario vazio
d[1] = 1 # add chave 1 e valor 1
print(d)
d['1'] = 2 # add chave 1 str e valor 1
print(d)
d[1] += 1 # 
print(d)

sum = 0 

for k in d:
    sum += d[k]

print(sum)
