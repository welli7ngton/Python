# Crie uma função chamada make_concatenator que recebe uma string inicial e retorna uma função interna. A função 
# interna deve receber uma nova string e concatená-la à string inicial. Teste a função retornada para criar uma 
# sequência de strings concatenadas.

def concatenador(palavra1):
    def concatenacao(palavra2):

        return palavra1 + palavra2
    return concatenacao

r = concatenador("teste1")

print(r("outrapalavra")) # saída = teste1outrapalavra
