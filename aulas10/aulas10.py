#1) Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). 
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome 
# estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

times = []

while len(times) <=10:
    nomes= input('digite um time: ')
    times.append(nomes)
leitura = input('qual time você deseja buscar? ')
if leitura in times:
    print('EU ACHEI!')
else:
    print('NÃO ACHEI!')
print(times)

# 2) Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

import random
from turtle import rt

numero =int(input('digite um número: '))
vetor = []

for i in range(30):
    t = random.randint(0,10)
    vetor.append((t))
rt = vetor.count(numero)
print(vetor)
print(rt)
