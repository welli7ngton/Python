# Dada uma lista de strings, crie uma nova lista com as strings que contêm apenas vogais 
# usando list comprehension.

lista = ['a', 'argumento', 'opcional', 'passado', 'várias', 'funções', 'iiii,', 'incluindo', 'função', 'max().', 'permite', 'especificar', 'função', 'comparação', 'ooouuu', 'iii', 'elementos', 'aa', 'processo', 'máximo.', 'contexto', 'expressão', 'aaaa', 'fornecida,', 'parâmetro', 'determinar', 'específica', 'dicionário', 'máximo', 'encontrado.', 'expressão', 'aaaeee', 'interna', 'lambda', 'x[key]', 'função', 'comparação', 'aplicada', 'dicionário', 'lista.', 'função', 'retorna', 'correspondente', 'eeee', 'dicionário.', 'função', 'parâmetro', 'definido', 'lambda', 'x[key],', 'comparar', 'valores', 'retornados', 'função', 'comparação', 'dicionário', 'assim,', 'encontrar', 'dicionário', 'máximo', 'especificada.', 'importante', 'ooouu', 'eu', 'presente', 'dicionários', 'lista.', 'uuu,', 'ocorrerá', 'tentar', 'acessar', 'inexistente.', 'Certifique-se', 'aeaeae', 'ouou', 'dicionários', 'resultados', 'i']


nl = [
    palavra 
    for palavra in lista 
    if all(letra.lower() in "aeiou" for letra in palavra)
    ]

print(nl)





