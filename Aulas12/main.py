#Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:Imprima o resultado da soma de todos os valores da matriz no terminal;E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3

from random import randint

A = []
B = []

for sequencia in range(10):
    sequencia = []

    for coluna in range(10):
        sequencia.append(randint(0, 1000))

    A.append(sequencia)

for matriz in A:
    print(matriz)

for sequencia in A:
    soma = sum(sequencia)
    print(soma)
    B.append(soma * 3)

print(B)