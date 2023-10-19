nota1 = float(input("digite a primeira nota: "))
if nota1 < 0 or nota1 > 10:
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("valor invalido, tente novamente: "))

nota2 = float(input("digite a segunda nota: "))
if nota2 < 0 or nota2 > 10:
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("nota invalida, tnte novamente: "))

media = (nota1 + nota2)/2
print(f"sua média é: {media:.2f}")
