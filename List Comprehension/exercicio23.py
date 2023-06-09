# Dada uma lista de strings, crie uma nova lista com as strings que são palíndromos usando list comprehension.

lista = [
    'parâmetro', 'Argumento','anotaram a data da maratona', 'opcional','amor a roma', 'passado', 'Avárias', 'Afunções', 'Python,', 'incluindo', 'função', 'max().', 'permite', 'especificar', 'Afunção', 'comparação', 'Apersonalizada', 'aplicada', 'elementos', 'Adurante', 'processo', 'máximo.', 'contexto', 'expressão', 'lamAbda', 'fornecida,', 'parâmetro','1110111', 'determinar','aaaa', 'específica', 'Adicionário','socorrammesubinoonibusemmarrocos', 'máximo', 'Aencontrado.', 'eAxpressão', 'AlAambda', 'AiAnterna', 'lambda', 'x[key]', 'fAunção', 'comparação','eva asse essa ave', 'Aplicada', 'Adicionário', 'lista.', 'função','lava esse aval', 'retorna', 'correspondente','acararajadadajararaca', 'especificada', 'dicionário.', 'Afunção', 'Aparâmetro', 'definido', 'lambda', 'x[key],', 'comparar', 'valores', 'retornados', 'funçAão', 'comparação','ole Maracuja caju caramelo', 'dicionário', 'Aassim,', 'encontrar', 'Adicionário', 'máximo', 'especificada.', 'importante', 'AfoArnecida', 'válida', 'presente', 'dicionários', 'lista.', 'contrário,', 'ocorrerá', 'Atentar', 'acessar', 'inexistente.', 'Certifique-se', 'Aespecificada','O lobo ama o bolo', 'consistente','subi no onibus', 'Adicionários', 'resultados', 'corretos.'
]

palindromos = [
    i
    for i in lista
    if i.lower().replace(" ","") == i[::-1].lower().replace(" ","")
]

print(palindromos)