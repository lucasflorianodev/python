#Aluno(a): Lucas Floriano da Silva

# Atividade Avaliativa - Questão 1

#[FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), 
#sendo que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raizes reais).
import math

a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))

delta = math.pow(b, 2) - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"X1 -> {x1:.2f}")
    print(f"X2 -> {x2:.2f}")
    print(f"Delta -> {delta}")
else:
    print("Reduza os valores de A e C!")

# Atividade Avaliativa - Questão 2
#[FORBELLONE, 2022] Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano,
#P(x1, y1) e Q(x2, y2), imprima a distância entre eles.

x1 = float(input("Digite x1:"))
x2 = float(input("Digite x2:"))
y1 = float(input("Digite y1:"))
y2 = float(input("Digite y2:"))

dist = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)
print(f"A distância entre os pontos é: {dist:.2f}")

# Atividade Avaliativa - Questão 3
#Elabore um algoritmo que leia o valor de dois números inteiros e a operacão aritimética desejada; calcule, então, a resposta adequada. 
#Utilize os símbolos da tabela a seguir para ler qual operacão aritmética escolhida.

val1 = int(input("Digite o 1° valor: "))
val2 = int(input("Digite o 2° valor: "))

result1 = val1 + val2
print("O resultado deu:", result1)

result2 = val1 - val2
print("O resultado deu:", result2)

result3 = val1 * val2
print("O resultado deu:", result3)

result4 = val1 / val2
print("O resultado deu:", result4)

result5 = val1 ** val2
print("O resultado deu:", result5)

# Atividade Avaliativa - Questão 4
#O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saudade para indicar a condição de peso de uma pessoa. 
#  A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a altura de uma adulto e mostre sua condição.


peso = float(input("qual é o seu peso? (kg) "))
altura = float(input("qual é a sua altura? (m) "))
IMC = peso / (altura ** 2)
print("o IMC dessa pessoa é de {:.1f}".format(IMC))

if IMC < 18.5:
    print("Voce está ABAIXO DO PESO normal")
elif 18.5<= IMC <25:
    print("Parabéns! você está na faixa de peso ideal!")
elif 25 <= IMC < 30:
    print("você está no SOBREPESO!")
elif 30 <= IMC <40:
    print("você está em OBESIDADE MORBIDA, Cuidado!")

# Atividade Avaliativa - Questão 5
#Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos
#: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo.

n = int(input("Quantos números?: "))
i = 0
a = 0
b = 0
c = 0
d = 0

while i < n: 
    numero = int(input("Insira um número: "))
    i = i + 1
    print(i)
    if numero < 0: 
        break
    if numero >= 0 and numero <= 25: 
        a = a + 1
    if numero >= 26 and numero <= 50: 
        b = b + 1
    if numero >= 51 and numero <= 75: 
        c = c + 1
    if numero >= 76 and numero <= 100: 
        d = d + 1
print
("Intervalo1: ",a)
print
("Intervalo2: ",b)
print
("Intervalo3: ",c)
print
("Intervalo4: ",d)

# Atividade Avaliativa - Questão 6
#Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

def main():
    A = int(input("Digite o valor de A: "))
    fat = 1
    i = 2
    while i <= A:
        fat = fat*i
        i = i + 1

    print("O valor de %d! é =" %A, fat)

main()
