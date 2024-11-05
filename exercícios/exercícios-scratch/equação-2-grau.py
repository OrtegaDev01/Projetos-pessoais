
a=float(input("Qual o Valor de a?"))
if a!=0:
    b=float(input("Qual o Valor de b?"))
    c=float(input("Qual o valor de c?"))
else:
    print("a ≠ 0")
    exit()

def square(y):
    calc=y*y
    return calc


def discriminante(a,b,c):
    Calculo= (b*b)+(-4*a*c)
    return Calculo


def raiz(g):
    retorno=g**(1/2)
    return retorno



def Bhaskara1(b,discre,a):
    xis= (-b+raiz(discre))/(2*a)
    return xis


def Bhaskara2(b,discre,a):
    xis2=(-b-raiz(discre))/(2*a)
    return xis2


delta=discriminante(a,b,c)



if delta>=0:

    x1=Bhaskara1(b,delta,a)
    x2=Bhaskara2(b,delta,a)

    print("x¹ é:" + str(x1))
    print("x² é:" + str(x2))

    print("Fórmula:ax²+bx+c=0")
else:
    print("Não há raízes reais nessa equação do 2º grau")
    print(delta)
    print("delta > -N")
    exit()    



if (a*square(x1))+(b*x1)+c==0  and (a*square(x2))+(b*x2)+c == 0 :
    print("As duas possibilidades são verdadeiras ")
    print("Resolução com x¹: " + str(a*square(x1)) + "+" + str(+b*x1) + "+" + str(c) + " = 0")
    print("Resolução com x¹: " + str(a*square(x1))+(b*x1)+str(c)+" = 0")
    print("Resolução com x²: " + str(a*square(x2)) + "+" + str(+b*x2) + "+" + str(c) + " = 0")
    print("Resolução com x²: " + str(a*square(x2)+(b*x2)+c)+" = 0")

elif(a*square(x1))+(b*x1)+c  == 0:
    print("A primeira possíbilidade é verdadeira,ou seja,segunda é falsa")
    print("Resolução com x¹: " + str(a*square(x1)) + "+" + str( b*x1 ) + "+" + str( c ) + " = 0")
    print("Resolução com x¹: " + str(a*square(x1)+(b*x1)+c)+" = 0")

else:
    print("A segunda possíbilidade é verdadeira,ou seja,a primeira é falsa") 
    print("Resolução com x²: " + str(a*square(x2)) + "+" + str(+b*x2) + "+" + str(c) + " = 0")
    print("Resolução com x²: " + str(a*square(x2)+(b*x2)+c)+" = 0")