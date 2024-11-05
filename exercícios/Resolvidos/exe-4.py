identificador = int(input("Qual o Gu do Aluno?"))
n1 = float(input("Qual nota o aluno obteve no 1º bimestre? "))
n2 = float(input("Qual nota o aluno obteve no 2º bimestre? "))
n3 = float(input("Qual nota o aluno obteve no 3º bimestre? "))

me = float(n1 + n2 + n3)

MA = ((n1 + n2 * 2 + n3 * 3 + me) / 7)

print("Gu do  aluno: " + str(identificador))
print("Nota do 1º Bimestre: " + str(n1))
print("Nota do 2º Bimestre: " + str(n2))
print("Nota do 3º Bimestre: " + str(n3))
print("Média dos exercícios: " + str(me))
print("Média de aproveitamento: " + str(MA))
conceito = 0
if MA >= 9:
    conceito = str("A")
if 7.5 < MA < 9:
    conceito = str("B")
if 6 > MA < 7.5:
    conceito = str("C")
if 4 > MA < 6:
    conceito = str("D")
if MA < 4:
    conceito = str("E")
print("Conceito: " + str(conceito))

# Completo
