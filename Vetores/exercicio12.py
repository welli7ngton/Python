#Problema "comerciante"
#Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. Para isto,
#mandou digitar um conjunto de N mercadorias, cada uma contendo nome, custo e venda
#das mesmas. Faça um programa que leia tais dados e determine e escreva quantas mercadorias
#proporcionaram:
#  lucro < 10%  
#  10% ≤ lucro ≤ 20%
#  lucro > 20%
#Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como
#o lucro total. 

                                            # custo = 100 |   custox = lucro * 100
                                            # lucro = x   |   x% = lucro * 100 /custo


n = int(input("digite a quantidade de produtos que serão digitados: "))

lucro1 = 0
lucro2 = 0
lucro3 = 0

nome : [str] = [0 for x in range(n)]
custo : [float] = [0 for x in range(n)]
venda : [float] = [0 for x in range(n)]
lucro : [float] = [0 for x in range(n)]
porcentagemlucro : [float] = [0 for x in range(n)]

for a in range(0,n):
    print(f"Produto {a + 1}:")
    nome[a] = input("Nome: ")
    custo[a] = float(input("Preço de compra: "))
    venda[a] = float(input("Preço de venda: "))
    lucro[a] = venda[a] - custo[a]
    porcentagemlucro[a] = (lucro[a] * 100) / custo[a]

for a in range(0,n):
    if porcentagemlucro[a] < 10:
        lucro1 += 1
    elif porcentagemlucro[a] >= 10 and porcentagemlucro[a] <= 20:
        lucro2 += 1
    else:
        lucro3 += 1   

print("RELATORIO: ")
print(f"Lucro abaixo de 10%: {lucro1}")
print(f"Lucro entre 10% e 20%: {lucro2}")
print(f"Lucro acima de 20%: {lucro3}")

print(f"Valor total de compra: {sum(custo):.2f}")
print(f"Valor total de venda: {sum(venda):.2f}")
print(f"Lucro total: {sum(lucro):.2f}")



