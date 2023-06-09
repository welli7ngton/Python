# Dada uma lista de strings, crie uma nova lista com as strings que têm um número par de caracteres usando list 
# comprehension.

l = ['parâmetro', 'argumento', 'opcional', 'passado', 'várias', 'funções', 'Python,', 'incluindo', 'função', 'max().', 'permite', 'especificar', 'função', 'comparação', 'personalizada', 'aplicada', 'elementos', 'durante', 'processo', 'máximo.', 'contexto', 'expressão', 'lambda', 'fornecida,', 'parâmetro', 'determinar', 'específica', 'dicionário', 'máximo', 'encontrado.', 'expressão', 'lambda', 'interna', 'lambda', 'x[key]', 'função', 'comparação', 'aplicada', 'dicionário', 'lista.', 'função', 'retorna', 'correspondente', 'especificada', 'dicionário.', 'função', 'parâmetro', 'definido', 'lambda', 'x[key],', 'comparar', 'valores', 'retornados', 'função', 'comparação', 'dicionário', 'assim,', 'encontrar', 'dicionário', 'máximo', 'especificada.', 'importante', 'fornecida', 'válida', 'presente', 'dicionários', 'lista.', 'contrário,', 'ocorrerá', 'tentar', 'acessar', 'inexistente.', 'Certifique-se', 'especificada', 'consistente', 'dicionários', 'resultados', 'corretos.']


nl = [palavra for palavra in l if len(palavra)%2 == 0]

print(nl)
