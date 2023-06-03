# Crie uma função chamada make_sequence_generator que recebe uma lista como argumento e retorna uma função 
# interna. A função interna deve iterar pela lista e retornar o próximo elemento da sequência a cada chamada. 
# Teste a função retornada para gerar diferentes sequências a partir da lista.

def make_sequence_generator(lista, pos=0):
    
    def sequencia():
        nonlocal pos
        proximo = lista[pos]
        pos += 1
        return proximo
    
    return sequencia
a = make_sequence_generator(["w","e","l","l","i","n","g","t","o","n"])

print(a())
print(a())
print(a())
print(a())
print(a())
print(a())
print(a())
print(a())
print(a())
print(a())

# saída:
# w
# e
# l
# l
# i
# n
# g
# t
# o
# n

