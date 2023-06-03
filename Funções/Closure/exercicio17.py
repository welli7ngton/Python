# Crie uma função chamada make_string_formatter que recebe um formato de string como argumento e retorna uma 
# função interna. A função interna deve receber os valores a serem formatados e retornar a string formatada. Teste 
# a função retornada para formatar diferentes strings com os valores corretos.

def make_string_formatter(palavra):
    def formatacao(a,b):
        nonlocal palavra
        palavra = palavra.replace(a,b)
        return palavra
    return formatacao 


a = make_string_formatter("well")

print(a("w","m"))
print(a("l","3"))

# saída:
# mell
# me33