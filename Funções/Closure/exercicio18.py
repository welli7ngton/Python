# Escreva uma função chamada make_multiplier_sequence que recebe uma lista de números como argumento e retorna uma 
# função interna. A função interna deve multiplicar cada elemento da lista pelo número fornecido e retornar a 
# lista resultante. Teste a função retornada para gerar sequências multiplicadas.



def make_multiplier_sequence(lista):
    def multiplicador(x):
        nova_lista = []
        for n in lista:
            nova_lista.append(n*x)
        return nova_lista
    return multiplicador

l = make_multiplier_sequence([1,2,3,4,5,6,7,8,9,10])

print(l(2))
print(l(3))
print(l(4))
print(l(10))

# saída:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]