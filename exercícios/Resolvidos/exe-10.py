"""
[Questão 10] Escrever um algoritmo que obtém via teclado 10 valores,
um de cada vez, e conta quantos deles estão no intervalo [10,20] e 
quantos deles estão fora do intervalo, escrevendo estas informações ao 
final da execução.
Lógica de Programação - Prof. Thiago S. Barcelos
"""
n=3
n_verificados=0
valores=0
intervalo=0
fora_intervalo=0
while n_verificados<n:
    valores=float(input("Me dê um valor: "))
    if  10<=valores<=20:
        intervalo+=1
    else:
        fora_intervalo+=1
    n_verificados+=1
print("Números que estão no intervalo entre 10 e 20: "+str(intervalo))
print("Números que não estão no intervalo entre 10 e 20: "+ str(fora_intervalo))