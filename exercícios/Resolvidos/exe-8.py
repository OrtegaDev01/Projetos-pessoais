"""
[Questão 8] Um posto de combustível vende três tipos de combustível: 
álcool, diesel e gasolina. O preço de cada litro dos combustíveis é 
apresentado na tabela abaixo. Faça um algoritmo que leia um carácter
que representa o tipo de combustível comprado (a, d ou g) e a 
quantidade em litros. O algoritmo deve imprimir o valor em reais a ser 
pago pelo combustível.
Combustível Preço por Litro
A – Álcool 1,7997
D – Diesel 0,9798
G – Gasolina 2,1009
Lógica de Programação - Prof. Thiago S. Barcelos
"""


valor=0
Alcool="a" or "A" 
Diesel="d" or "D"
Gasolina="g" or "G"
print("A --> Álcool")
print("D --> Diesel")
print("G --> Gasolina")
combus=str(input("Qual o tipo de combústivel? "))
litros=float(input("Quantos litros?"))
if combus==Alcool:
   valor=litros*1.7997
if combus==Diesel:
   valor=litros*0.9798
if combus==Gasolina:
   valor=litros*2.1009
print("Valor Total: "+ "R$" +str(round(valor,2)))






