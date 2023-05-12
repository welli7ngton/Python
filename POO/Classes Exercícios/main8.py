from exercicio8 import conta


while True:
    n = input("digite seu nome: ")
    nconta = int(input("digite o número da conta: "))

    p1 = conta(nconta, n)
    p1.mostrainfo()


    op = int(input("qual operação deseja fazer: (1)alterar nome, (2)depósito, (3)saque, (4)encerrar: "))

    if op == 1:
        p1.alteranome()
        p1.mostrainfo()
    elif op == 2:
        p1.deposito()
        p1.mostrainfo()
    elif op == 3:
        p1.saque()
        p1.mostrainfo()
    elif op == 4:
        break

    print("deseja verificar mais uma pessoa? (S/N)")
    op = input()

    if op.upper() == 'N':
        break
