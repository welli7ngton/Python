nome = input("digite seu nome: ")

sexo = input("digite seu sexo:")

idade = int(input("digite sua idade: "))

if sexo == 'feminino' and idade < 25:
    print(f"{nome} Aceita")
else:
    print("Não aceita")
