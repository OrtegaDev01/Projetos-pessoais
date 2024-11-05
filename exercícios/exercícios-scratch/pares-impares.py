n=int(input("Quantos Números?"))
contador=0
pares=0
impar=0

def resto(xy):
    Divisão=xy % 2 == 0
    return Divisão


while n>contador:
    Number=int(input("digite um número: "))
    if resto(Number):
        pares +=1
    else:
        impar+=1
    contador +=1
print("quantidade de pares: " + str(pares))
print("quantidade de impares: " + str(impar))


    