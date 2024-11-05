n=int(input("Quantos Itens?"))
nv=0
especial=0
total_produtos=0
while nv < n:
    produtos=int(input("Qual o valor do item?"))
    if produtos>100:
        especial+= 1
    total_produtos += produtos
    nv += 1
print("Valor total: " "R$"+str(total_produtos))
if especial>=2:
    print("Parabéns,você ganhou um grande desconto")        
    print("Valor com Desconto: " +"R$" + str(int(total_produtos-(total_produtos*0.3))))