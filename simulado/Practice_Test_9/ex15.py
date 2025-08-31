# what will be the output of the following code?
def fun(a=1, b=3):
    return a * b
print(fun(b=2))


"""
O restado será 2
pois quando utilizamos parametros o valor ja está sendo passo por default

no caso é a=1 e b=3 

na chamada da função passamos para b=2

e quando chamamos a função executamos a conta que é de a * b que no caso esta valendo 2
"""
