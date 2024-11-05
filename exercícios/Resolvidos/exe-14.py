"""
[Questão 14] Suponha que uma escola possui N alunos. Sendo conhecidas as idades
de cada um dos alunos, via digitação pelo teclado pede-se para calcular e imprimir:
a) A quantidade de alunos eleitores (idade mínima para votar 16 anos)
b) A média de idade dos não eleitores.
"""
quantidade_alunos=int(input("Há quantos alunos?  "))

eleitores=0
n_eleitores=0

Alunos_verificados=0

while Alunos_verificados<quantidade_alunos:
    idade_alunos = int(input("Qual a idade do aluno? "))
    if idade_alunos>=16:
        eleitores+=1
    else:
        n_eleitores+=1
    Alunos_verificados+=1

media=(n_eleitores/quantidade_alunos)

print("Quantidade de eleitores: " + str(eleitores))
print("Media das pessoas que não são eleitores: "+str(media))