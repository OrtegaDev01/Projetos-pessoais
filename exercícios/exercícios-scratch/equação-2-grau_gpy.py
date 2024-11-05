import math

a = float(input("Qual o Valor de a? "))
if a != 0:
    b = float(input("Qual o Valor de b? "))
    c = float(input("Qual o valor de c? "))
else:
    print("a ≠ 0")
    exit()

def discriminante(a, b, c):
    return (b * b) - (4 * a * c)

def raiz(g):
    return math.sqrt(g)

def bhaskara1(b, delta, a):
    return (-b + raiz(delta)) / (2 * a)

def bhaskara2(b, delta, a):
    return (-b - raiz(delta)) / (2 * a)

delta = discriminante(a, b, c)

if delta >= 0:
    x1 = bhaskara1(b, delta, a)
    x2 = bhaskara2(b, delta, a)

    print(f"x¹ é: {x1:.2f}")
    print(f"x² é: {x2:.2f}")
    print("Fórmula: ax² + bx + c = 0")
else:
    print("Não há raízes reais nessa equação do 2º grau")
    print(f"Delta: {delta:.1f}")
    exit()

def verifica_raiz(a, b, c, x):
    return a * (x ** 2) + b * x + c == 0

if verifica_raiz(a, b, c, x1) and verifica_raiz(a, b, c, x2):
    print("As duas possibilidades são verdadeiras")
    print(f"Resolução com x¹: {a:.2f}*({x1:.2f}²) + {b:.2f}*({x1:.2f}) + {c:.2f} = 0")
    print(f"Resolução com x²: {a:.2f}*({x2:.2f}²) + {b:.2f}*({x2:.2f}) + {c:.2f} = 0")
elif verifica_raiz(a, b, c, x1):
    print("A primeira possibilidade é verdadeira, ou seja, a segunda é falsa")
    print(f"Resolução com x¹: {a:.2f}*({x1:.2f}²) + {b:.2f}*({x1:.2f}) + {c:.2f} = 0")
else:
    print("A segunda possibilidade é verdadeira, ou seja, a primeira é falsa")
    print(f"Resolução com x²: {a:.2f}*({x2:.2f}²) + {b:.2f}*({x2:.2f}) + {c:.2f} = 0")
