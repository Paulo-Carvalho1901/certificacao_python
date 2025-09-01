"""
1. end=''

Propósito: Controla o que é impresso após todos os itens que você passou para a função print().

Comportamento padrão: Por padrão, a função print() adiciona um caractere de nova linha (\n) ao final da saída. Isso faz com que a próxima chamada print() comece na linha seguinte.

end='': Ao usar end='', você está dizendo à função print() para substituir o caractere de nova linha padrão por uma string vazia. Isso faz com que a próxima chamada print() continue na mesma linha.

Exemplo:
"""
# print('Olá', end=' ')
# print('Mundo!')

print('Olá', 'mundo!', sep="-")
print(list('hello'))
