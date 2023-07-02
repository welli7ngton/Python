# Vamos implementar um programa de agenda de contatos. O programa terá a opção
# de cadastro, consulta e exclusão de contato.

# Todo contato terá as opções de acordo com a atividade DICIONÁRIO Q1
# (UM CONTATO DE UMA AGENDA).

# No programa principal você irá criar um dicionário chamado de agenda. Esse
# dicionário irá representar a agenda. Nesse dicionário a chave será o nome da
# pessoa e o valor será o dicionário com os dados dela. A cada novo contato
# adicionado, você irá criar um dicionário que irá armazenar as informações do
# contato.

# INTERFACE COM O USUÁRIO
# O programa terá um menu de opções principal como mostrado abaixo:

# Bem-vindo ao programa Agenda de Contato

# Digite 1 para cadastrar um contato

# Digite 2 para consultar um contato

# Digite 3 para excluir um contato

# Digite 0 para sair do programa

# Quando o usuário digitar opção 1, o programa irá solicitar os dados do novo
# contato e irá fazer o cadastro. Depois retorna ao menu principal. ATENÇÂO:Não
# será permitido o cadastro de dois contatos com o mesmo nome.Então seu
# programa
# deve informar ao usuário se por acaso um contato com o nome já cadastrado.

# Quando o usuário digitar opção 2, o programa irá solicitar o nome do contat
# que
# deseja consultar. Após receber o nome o programa irá exibir na tela os dados
# do
# contato. Se por acaso o usuário digitar um nome se contato não salvo, o
# programa
# irá exibir uma mensagem dizendo que o contato não existe. Em qualquer uma das
# duas situações, após o programa retorna ao menu principal.

# Quando o usuário digitar opção 3, o programa irá solicitar o nome do contato
# que
# deseja excluir. Após receber o nome o programa irá exibir na tela uma
# mensagem
# informando que a exclusão foi realizada com sucesso. Se por acaso o usuário
# digitar um nome se contato não salvo, o programa irá exibir uma mensagem
# dizendo
# que o contato não existe. Em qualquer uma das duas situações, após o programa
# retorna ao menu principal.
# Quando o usuário digitar opção 0 o programa se encerra

def cadastra_contato(agenda):
    nome = input("digite seu nome: ").title()
    if nome in agenda:
        print("Já existe um contato cadastrado com esse nome.")
        return False
    idade = int(input("digite sua idade: "))
    peso = float(input("digite seu peso: "))
    cidade = input("digite sua cidade: ").title()
    tel = input("digite seu telefone: ")
    apelido = input("digite seu apelido: ")
    print("Dados cadastrados com sucesso.")

    return nome, idade, peso, cidade, tel, apelido


def consulta_cadastro(agenda):
    n = input("Digite o nome da pessoa que você quer procurar: ")
    if n not in agenda:
        print("O contato não foi esncontrado.")
        return False
    print(f"\nInformações de: {n}")
    print(agenda[n])


def excluir_contato(agenda):
    n = input("Digite o contato para excluir: ")
    if n not in agenda:
        print("O contato não existe.")
        return False
    agenda.pop(n)
    print("Contato excluido.")
    return True


agenda = {
    "Wellington": {
        "Idade": 20,
        "Peso": 55.0,
        "Cidade": "Morada Nova",
        "Telefone": "88 9 8176-2299",
        "Apelido": "welli7ngton"},
    "Maria Helena": {
        "Idade": 19,
        "Peso": 65.0,
        "Cidade": "Morada Nova",
        "Telefone": "99 9 9999-8888",
        "Apelido": "helena"}
    }


while True:
    print("\nBem-vindo ao programa Agenda de Contato")
    print("Digite (1) para cadastrar um contato")
    print("Digite (2) para consultar um contato")
    print("Digite (3) para excluir um contato")
    print("Digite (0) para sair do programa")
    r = input("Opeção: ")
    if r == "0":
        break

    elif r == "1":
        nome, idade, peso, cidade, tel, apelido = cadastra_contato(agenda)
        agenda[nome] = {"Idade": idade,
                        "Peso": peso,
                        "Cidade": cidade,
                        "Telefone": tel,
                        "Apelido": apelido
                        }
    elif r == "2":
        consulta_cadastro(agenda)

    elif r == "3":
        excluir_contato(agenda)
