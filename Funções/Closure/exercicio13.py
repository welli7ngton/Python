# Escreva uma função chamada make_repeater que recebe uma string como argumento e retorna uma função interna. A 
# função interna deve receber um número n e repetir a string fornecida n vezes, separadas por espaços. Teste a 
# função retornada para repetir uma string um determinado número de vezes.

def make_repeater(palavra = ''):
    def repeater(x):

        return f"{(palavra + ' ')* x}"

    return repeater

p = make_repeater("teste")

print(p(6))

p = make_repeater("wellington")

print(p(3))

# saída: 
# teste teste teste teste teste teste 
# wellington wellington wellington