"""
[Questão 15] A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
a) média do salário da população;
b) média do número de filhos;
c) maior salário;
d) percentual de pessoas com salário até R$ 100,00.
O final da leitura de dados se dará com a entrada de um salário negativo
"""
media_filhos=0
media_salario=0
percentual_salario=0
quantidade_pessoas=int(input("Há quantas pessoas na cidade?"))
pessoas_verificadas=0
quantidade_filhos=0
salario_total=0
while pessoas_verificadas<quantidade_pessoas:
    salario=float(input("Qual o seu  salário? "))
    salario_total+=salario
    quantidade_filhos=int(input("Quantos filhos você tem?"))
    pessoas_verificadas+=1

media_filhos+=(quantidade_filhos/quantidade_pessoas)
media_salario+=(salario_total+quantidade_pessoas)/2

percentual_salario+=(salario_total/quantidade_pessoas)

print("Média de filhos: "+str(media_filhos))
print("Média  do salário das pessoas na cidade: "+str(media_salario))
print("Percentual do")





