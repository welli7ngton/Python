"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

cpf = "777.710.600-72"
print("CPF:", cpf)
cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")
cpf = cpf[:9]

somas = 0
mult = 10
for a in range(0, 9):
    somas += int(cpf[a]) * mult
    mult -= 1

somas *= 10

resto = somas % 11

resultado = 0 if resto > 9 else resto

print("O primeiro dígito do CPF é", resultado)

cpf = cpf + str(resultado)

mult = 11
somas2 = 0

for digito in cpf:
    somas2 += int(digito) * mult
    mult -= 1

somas2 *= 10
resto2 = somas2 % 11

resultado2 = resto2 if resto2 <= 9 else 0

print("O segundo dígito do CPF é", resultado2)
