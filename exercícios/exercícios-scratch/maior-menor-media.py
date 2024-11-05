"""
[Questão 1] Fazer um programa que recebe 3 valores não
inteiros do usuário e mostra o maior deles, o menor deles e a
média
"""

neutro=0
numerous=3
numerous_verificados=0
menor=0
resposta=0
maior=float(input("Me dê um número aleatório: "))

while numerous>numerous_verificados:
    resposta=float(input("Me dê um número: "))
    if resposta>maior:
        maior=resposta
    if resposta<menor:
        menor=resposta
    if menor<resposta<maior:
        neutro=resposta
    numerous_verificados+=1
print("maior: "+ str(maior))
print("menor :"+ str(menor))
print("Neutro :"+ str(neutro))
print("Média: "+ str((maior+menor+neutro)/numerous))