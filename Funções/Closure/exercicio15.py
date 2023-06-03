# Escreva uma função chamada make_logger que recebe um prefixo de log como argumento e retorna uma função interna. 
# A função interna deve receber uma mensagem como argumento e imprimir a mensagem junto com o prefixo de log. 
# Teste a função retornada para registrar diferentes mensagens com o prefixo correto.

def make_logger(log):
    def mensagem(msg):
        print(log, msg)
    return(mensagem)

m1 = make_logger("well")
m2 = make_logger(1101)
m1("teste de mensagem 1")
m1("segundo teste")
m2("testes testes")
m2("okokok")

# saída:
# well teste de mensagem 1
# well segundo teste
# 1101 testes testes
# 1101 okokok