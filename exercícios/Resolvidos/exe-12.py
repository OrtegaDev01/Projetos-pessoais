"""
[Questão 12] Dados a idade e o peso de "n" pessoas, calcular e imprimir a
médias dos pesos das pessoas que pertençam a uma mesma faixa etária.
As faixas etárias são: de 1 a 10 anos, de 11 a 20 anos, de 21 a 30 anos e
maiores de 30 anos
"""


pessoas=int(input("Há quantas pessoas?"))
pessoas_verificadas=0
de1_a_10=0
de11_a_20=0
de21_a_30=0
maior_30=0
media1a10=0
media11a20=0
media21a30=0
media_maior_30=0
peso=0

while pessoas>pessoas_verificadas:
    idade=int(input("Qual a Idade?"))
    peso=int(input("Qual o peso?"))
    if 1>= idade <=10:
        de1_a_10+=1
    if 11>+ idade <=20:
        de11_a_20+=1
    if 21>= idade <=30:
        de21_a_30+=1
    if idade>30:
        maior_30+=1
    pessoas_verificadas+=1

if de1_a_10>0:
    media1a10=float(peso/de1_a_10)
    print("Média das pessoas com idade de 1 a 10 anos: " + str(media1a10))
if de11_a_20>0:
    media11a20 =float(peso / de11_a_20)
    print("Média das pessoas com idade de 11 a 21 anos: " + str(media11a20))
if de21_a_30>0:
    media21a30 = float(peso / de21_a_30)
    print("Média das pessoas com idade de 21 a 30 anos: " + str(media21a30))
if maior_30>0:
    media_maior_30 = float(peso / maior_30)
    print("Média das pessoas com idade maiores que 30 anos: " + str(media_maior_30))






