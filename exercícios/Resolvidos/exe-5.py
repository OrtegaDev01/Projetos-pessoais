"""
[Questão 5] Escreva um programa que leia o código de um aluno e suas
três notas. Calcule a média ponderada do aluno, considerando que o
peso para a maior nota seja 4 e para as duas restantes, 3. Mostre o
código do aluno, suas três notas, a média calculada e uma mensagem
4
"APROVADO" se a média for maior ou igual a 5 e "REPROVADO" se a
média for menor que 5.
"""
Gu=int(input("Qual o Gu do Aluno? "))
n1=float(input("Primeira nota: "))
n2=float(input("Segunda nota:  "))
n3=float(input("Terceira nota: "))

mp=0

if n1>n2 and  n1>n3:
    mp=((n1*4)+(n2*3)+(n3*3))/10
if n2>n1 and n2>n3:
    mp=((n2*4)+(n1*3)+(n3*3))/10
if n3>n1 and n3>n2:
    mp=((n3*4)+(n1*3)+(n2*3))/10

print("Gu do aluno: " + str(Gu))
print("Primeira nota "+ str(n1))
print("Segunda nota "+ str(n2))
print("Terceira nota "+ str(n3))
print("Média ponderada do aluno: " + str(mp))
if mp>=5:
    print("O aluno  foi aprovado")
else:
    print("O aluno foi reprovado")

