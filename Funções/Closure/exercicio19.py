# Crie uma função chamada make_positive_filter que retorna uma função interna. A função interna deve receber uma 
# lista e filtrar apenas os números positivos. Teste a função retornada para filtrar listas com diferentes números.

def make_positive_filter():
    def filtro(l=[]):
        positivos = []
        for n in l:
            if n %2 == 0:
                positivos.append(n)
        return positivos
    return filtro

a = make_positive_filter()

print(a([1,2,3,4,5,6,7,8]))

print(a([7,9,5,3]))

print(a([2,0,8,10,12,4,56]))

# saída:
# [2, 4, 6, 8]
# []
# [2, 0, 8, 10, 12, 4, 56]