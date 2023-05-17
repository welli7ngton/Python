#Ler o nome e o valor de uma determinada mercadoria de uma loja. Sabendo que o
#desconto para pagamento a vista ` e de 10% sobre o valor total, calcular o valor a ser ´
#pago a vista. Escrever o nome da mercadoria, o valor total, o valor do desconto e o valor `
#a ser pago a vista.


dados = str(input("digite o nome e valor da mercadoria :")).strip()

lista = dados.split()

nome = lista[0]
valor = float(lista[1])

desconto = valor * 0.1
avista = valor - desconto

print(f"nome: {nome}")
print(f"valor total: {valor}")
print(f"desconto: {desconto:.2f}")
print(f"valor á vista: {avista}")




