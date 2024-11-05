"""
[Questão 11] Obter via teclado a idade de n(número) pessoas, calcular e informar
a quantidade de pessoas maiores de idade (idade ≥ 18).
"""


pessoas=int(input("Há quantas pessoas?"))
Pessoas_verificadas=0
maiores=0
menores=0

while Pessoas_verificadas<pessoas:
    idade=int(input("Qual a idade?"))
    if idade >=18:
        maiores+=1
    else:
        menores+=1
    Pessoas_verificadas+=1
print("Maiores de 18 anos: " + str(maiores))
print("Menores de 18 anos: " + str(menores))


