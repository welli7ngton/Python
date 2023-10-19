nota1 = float(input("digite primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
media = (nota1 + nota2)/2

while nota1 > 0 and nota1 < 10 and nota2 > 0 and nota2 < 10:
    print(f"sua média é: {media:.2f}")
    nota1 = float(input("digite primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))
    media = (nota1 + nota2)/2
