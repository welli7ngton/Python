# Crie uma classe chamada "Pessoa" com atributos de instância "nome", "idade" e "endereço" e um método 
# "adicionar_email" que permite adicionar um email à lista de emails da pessoa.

class Pessoa:
    
    

    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.__emails = []
    
    def add_email(self,email):
        # email = input("Digite o email que deseja salvar: ")
        self.__emails.append(email)

    def listar_emails(self):
        print()
        print("="*20,"Emails","="*20)
        for email in self.__emails:
            print("\tEmail:",email)
        print("="*48)

p1 = Pessoa("Wellington",20,"Rua1")
p2 = Pessoa("Maria",21,"Rua2")
p2.add_email("mariahelena123@gmail.com")
p2.add_email("mariahelena16565@gmail.com")
p1.add_email("wellingtonasilva40@gmail.com")
p1.add_email("wellingtonasilva3@gmail.com")
p2.add_email("mariahelena1@gmail.com")
p1.add_email("wellingtonasilva5@gmail.com")
p2.add_email("mariahelena1287@gmail.com")
p2.add_email("mariahelena12313@gmail.com")
p1.add_email("wellingtonasilva45@gmail.com")
p1.add_email("wellingtonasilva9@gmail.com")
p2.add_email("mariahelena1999@gmail.com")

p1.listar_emails()
p2.listar_emails()

