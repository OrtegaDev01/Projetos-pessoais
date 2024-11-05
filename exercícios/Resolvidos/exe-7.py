'''


[Questão 7] Tendo como dados de entrada a altura e o sexo de uma 
pessoa (M - masculino e F - feminino), construa um programa que calcule 
seu peso ideal, utilizando as fórmulas a seguir, e indica se a pessoa está 
acima ou abaixo do seu peso ideal
para homens: (72.7*h) - 58
para mulheres: (62.1*h) - 44.7
'''


peso=float(input("Qual o seu peso? "))
alt=float(input("Qual a sua Altura?"))
sex=str(input("Qual o seu Gênero?"))
PesoIdeal=0

if sex=="M":
    PesoIdeal=float((72.7*alt) - 58)
if sex=="F":
    PesoIdeal=float((62.1*alt) -44.7)
    
if peso>PesoIdeal:
    print("Você esta acima do seu peso ideal")
if peso<PesoIdeal:
    print("Você esta abaixo do seu peso ideal")

