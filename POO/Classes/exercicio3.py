#3. Crie uma classe representando os alunos de um determinado curso. A classe deve
#conter os atributos matrıcula do aluno, nome, nota da primeira prova, nota da segunda
#prova e nota da terceira prova. Crie metodos para acessar o nome e a media do aluno. 
#(a) Permita ao usuario entrar com os dados de 5 alunos. 
#(b) Encontre o aluno com maior media geral. 
#(c) Encontre o aluno com menor media geral 
#(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
#aprovacao.


class alunos_redes:

    nomes = []

    def __init__(self):
        
        self.matricula = int(input("digite sua matricula: "))
        self.nome = input("digite seu nome: ")
        self.nomes.append(self.nome)
        self.nota1 = float(input("digite sua 1° nota: "))
        self.nota2 = float(input("digite sua 2° nota: "))
        self.nota3 = float(input("digite sua 3° nota: "))    

        

        return 
    
    def verifica_aprovacao(self):
        
        media = (self.nota1 + self.nota2 + self.nota3) / 3

        return media

    def verifica_medias(self,vetormedias):
        
        menor = 100
        maior = 0
        for a in range(len(vetormedias)):
            if vetormedias[a] > maior:
                maior = vetormedias[a]
                nomemaior = self.nomes[a]

            if vetormedias[a] < menor:
                menor = vetormedias[a]
                nomemenor = self.nomes[a]
        return (maior, menor, nomemaior, nomemenor)