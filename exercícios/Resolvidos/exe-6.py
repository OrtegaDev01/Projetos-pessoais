"""
[Dicionário]
n1 →Nota do primeiro bimestre
n2 →Nota do segundo bimestre
n3 →Nota do terceiro bimestre
n4 →Nota do quarto bimestre
ma →Média aritmética do aluno
pa →Presença do aluno
pn →Media de presença do aluno
si →Situação do aluno
nx →Nota do exame
mxf →Média do exame final
"""


sit=0
n1=float(input("Qual nota o aluno obteve no 1º bimestre?"))
n2=float(input("Qual nota o aluno obteve no 2º bimestre?"))
n3=float(input("Qual nota o aluno obteve no 3º bimestre?"))
n4=float(input("Qual nota o aluno obteve no 4º bimestre?"))
nf=float(input("O aluno Faltou Quantas Vezes no ano?"))
ma=float((n1+n2+n3+n4))/4
Aulas=int(input("Qual a quantidade total de aulas da instituição?"))
pa=float(-nf + Aulas)
pn= round(float(pa/Aulas), 4) * 100
print("Média do aluno: " + str(ma))
print("presença: " + str(round(pn,2)) + "%")
if ma>=6 and pn>=75:
    print("O aluno foi aprovado")
    exit()
if ma>=6 and pn<75:
    print("O aluno reprovou por falta")
    exit()
if ma<6 and pn>=75:
    print("O aluno está sujeito a exame")
    sit=str("exame")
if sit == "exame":
    nx=float(input("Qual a nota do exame final?"))
    mxf=float(ma + nx)/2
    if mxf>=6:
        print("O aluno foi aprovado pelo exame")
        exit()
    else:
        print("O aluno foi reprovado no exame")
        exit()
