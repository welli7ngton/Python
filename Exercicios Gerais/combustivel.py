cod=int(input("digite um codigo (1, 2, 3) ou 4 para encerrar: "))

alcool = 0
gasolina = 0
diesel = 0


while cod != 4:
    cod = int(input("digite um codigo (1, 2, 3) ou 4 para encerrar: "))
    if cod == 1:
        alcool += 1
    elif cod == 2:
        gasolina += 1
    elif cod == 3:
        diesel += 1


print("muito obrigado")
print(f"alcool: {alcool}")
print(f"gasolina: {gasolina}")
print(f"diesel: {diesel}")

