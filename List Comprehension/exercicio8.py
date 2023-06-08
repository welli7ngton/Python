# Dada uma lista de palavras, crie uma nova lista com as palavras que começam com a letra 
# "A" usando list comprehension.

l = ['parâmetro', 'Argumento', 'opcional', 'passado', 'Avárias', 'Afunções', 'Python,', 'incluindo', 'função', 'max().', 'permite', 'especificar', 'Afunção', 'comparação', 'Apersonalizada', 'aplicada', 'elementos', 'Adurante', 'processo', 'máximo.', 'contexto', 'expressão', 'lamAbda', 'fornecida,', 'parâmetro', 'determinar', 'específica', 'Adicionário', 'máximo', 'Aencontrado.', 'eAxpressão', 'AlAambda', 'AiAnterna', 'lambda', 'x[key]', 'fAunção', 'comparação', 'Aplicada', 'Adicionário', 'lista.', 'função', 'retorna', 'correspondente', 'especificada', 'dicionário.', 'Afunção', 'Aparâmetro', 'definido', 'lambda', 'x[key],', 'comparar', 'valores', 'retornados', 'funçAão', 'comparação', 'dicionário', 'Aassim,', 'encontrar', 'Adicionário', 'máximo', 'especificada.', 'importante', 'AfoArnecida', 'válida', 'presente', 'dicionários', 'lista.', 'contrário,', 'ocorrerá', 'Atentar', 'acessar', 'inexistente.', 'Certifique-se', 'Aespecificada', 'consistente', 'Adicionários', 'resultados', 'corretos.']


l2 =[p for p in l if p.startswith("A")]

print(l2)