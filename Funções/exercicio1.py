#Faça	uma	função	que calcule a	média	de	um	aluno	de	acordo	com	o	critério	definido	
#neste	curso.	Além	disso,	 faça	uma	segunda	 função	que	informe	o	status	do	aluno	de	
#acordo	com	a	tabela	a	seguir:
#   Nota	acima	de	6	à “Aprovado”
#   Nota	entre	4	e	6	à Conceito	“Verificação	Suplementar”
#   Nota	abaixo	de	4	à Conceito	“Reprovado”




def calculamedia(nota1,nota2):
    media = 0
    media = (nota1 + nota2) / 2

    return(media)

print("Digite suas notas n1 e n2:")
n1 = float(input())
n2 = float(input())

resultado = calculamedia(n1, n2)

if resultado >= 6:
    print("Aprovado.")
elif resultado < 6 and resultado >= 4:
    print("Verificação Suplementar.")
else:
    print("Reprovado.")