# Dada uma lista de strings, crie uma nova lista com as strings que têm apenas 
# letras maiúsculas usando list comprehension.

def upper(palavra):
    r = None
    for i in palavra:
        if i == i.upper():
            r = True
        else:
            r = False
            break
    return r


lista = [
    'parâmetro', 'ARGUMENTO', 'OPCIONAL', 'passado', 'várias', 'funções', 'PYTHON,', 'incluindo', 'função', 'max().', 'PERMITE', 'especificar', 'função', 'COMPARACAO', 'personalizada', 'aplicada', 'ELEMENTOS', 'DURANTE', 'processo', 'máximo.', 'contexto', 'EXPRESSAO', 'lambda', 'fornecida,', 'parâmetro', 'determinar', 'específica', 'dicionário', 'MAXIMO', 'encontrado.', 'expressão', 'lambda', 'interna', 'LAMBDA', 'x[key]', 'função', 'comparação', 'APLICADA', 'DICIONARIO', 'LIST.', 'função', 'RETORNA', 'correspondente', 'especificada', 'dicionário.', 'função', 'parâmetro', 'DEFINICAO', 'lambda', 'x[key],', 'COMPARAR', 'VALORES', 'retornados', 'FUNCAO', 'comparação', 'DICIONARIO', 'assim,', 'encontrar', 'dicionário', 'máximo', 'especificada.', 'IMPORTANTE', 'fornecida', 'VALIDA', 'presente', 'dicionários', 'LISTA.', 'contrário,', 'ocorrerá', 'TENTAR', 'ACESSAR', 'INEXISTENTE.', 'Certifique-se', 'ESOECIFICADA', 'consistente', 'dicionários', 'resultados', 'CORRETOS.'
]


lista_upper = [
    palavra 
    for palavra in lista
    if upper(palavra)
]

print(lista_upper)