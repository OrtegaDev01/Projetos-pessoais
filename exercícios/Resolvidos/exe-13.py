"""
[Questão 13] Uma loja utiliza os seguintes códigos para as transações de cada dia:
"v"- para compras à vista
"p"- para compras a prazo
O usuário digitará uma lista de transações contendo o valor de cada compra e o
respectivo código da transação. Faça um programa que calcule e imprima:
a) Valor total das compras à vista;
b) Valor total das compras a prazo;
c) Valor total das compras efetuada;
Sabe-se que são efetuadas 25 transações por dia
"""


compras_limit=24
compra_verificadas=0


valor_vista=0
valor_prazo=0
valor_total=0
v="vista" or "A vista" or "Vista"
p="prazo" or "A prazo" or "Vista"

while compras_limit>compra_verificadas:
    tipo_compra=str(input("A vista ou a prazo? "))
    if tipo_compra== v:
        valor_vista+=float(input("Qual o valor da compra? "))
    if tipo_compra== p:
        valor_prazo+=float(input("Qual o valor da compra? "))
    compra_verificadas+=1

valor_total+=valor_prazo+valor_vista
print("Valor total das compras a vista: "+"R$"+ str(valor_vista))
print("Valor total das compras a prazo: "+"R$"+ str(valor_prazo))
print("Valor total das compras efetuadas: "+"R$"+ str(valor_total))