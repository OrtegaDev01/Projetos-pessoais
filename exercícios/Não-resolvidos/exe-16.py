"""
[Questão 16] Escreva um algoritmo que lê um número
natural e verifica se o mesmo é primo ou não.
"""

from sympy import isprime



Number=int(input("Me dê um número Natural:  "))
if isprime(Number) :
    print("O Número é primo")
else:
    print("O número não é primo")



