#teste de mesa questão 2

from cgi import print_form


ano = 2022

if ano < 2022:
    print("não será necessário seu voto esse ano, o TSE agradece sua preocupação")
elif ano > 2007:
    print("O seu voto ainda não é necessário, o TSE agradece sua preocupação, nos vemos em breve!")
elif ano <= 2006:
    print("seu voto é opcional, caso queira votar esse ano, peça ajuda ao seu responsável e procure o colégio mais próximo no dia da votação para efetuar seu voto!")
else:
    print("seu voto é necessário! nos vemos em breve!")