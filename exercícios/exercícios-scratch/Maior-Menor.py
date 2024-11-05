N=int(input("Me dê um Número: "))
Maior=int(input("Me dê um valor: "))
Menor=Maior
Contador=1


while N>Contador:
    b=int(input("Me dê um valor:"))
    if b>Maior:
        Maior=b
    if b<Menor:
        Menor=b
   
    Contador += 1
print("Menor:" + str(Menor))    
print("Maior:" + str(Maior))













