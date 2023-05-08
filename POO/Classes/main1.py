from exercicio1 import Pessoa
vetdados = [" "," "," "]

qtdp = int(input("quantas pessoas quer cadastrar? "))

for a in range(qtdp):
    print("digite seus dados: nome, idade e endereço")
    for b in range(3):
        vetdados[b] = input()

    p = Pessoa(vetdados[0], vetdados[1], vetdados[2])
    print(f"dados da pessoa {a+1}: ")
    print(f"{p.nome}, {p.idade}, {p.endereco}")
    



    r = input("deseja mudar endereço?(S/N)")

    if r.upper() == "S":

        p.muda_endereco()
        print("esses são os dados da pessoa cadastrada: ")
        print(f"{p.nome}, {p.idade}, {p.endereco}")

    else:
        print("esses são os dados da pessoa cadastrada: ")
        print(f"{p.nome}, {p.idade}, {p.endereco}")