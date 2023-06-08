# Dada uma lista de palavras, crie uma nova lista com as palavras que têm mais de 5 letras 
# usando list comprehension.
s = '''
O parâmetro key é um argumento opcional que pode ser passado para várias funções em Python, incluindo a função max(). Ele permite especificar uma função de comparação personalizada que será aplicada aos elementos da lista durante o processo de busca pelo valor máximo.

No contexto da expressão lambda fornecida, o parâmetro key é usado para determinar a chave específica de cada dicionário na lista pela qual o valor máximo será encontrado.

A expressão lambda interna lambda x: x[key] é a função de comparação que será aplicada a cada dicionário x na lista. Essa função retorna o valor correspondente à chave especificada (key) para cada dicionário.

Ao usar a função max() com o parâmetro key definido como lambda x: x[key], ela irá comparar os valores retornados pela função de comparação para cada dicionário e, assim, encontrar o dicionário com o valor máximo para a chave especificada.

É importante notar que a chave fornecida deve ser uma chave válida presente em todos os dicionários da lista. Caso contrário, ocorrerá um erro ao tentar acessar uma chave inexistente. Certifique-se de que a chave especificada seja consistente em todos os dicionários da lista para obter resultados corretos.
'''
l = s.split()

l2 = [p for p in l if len(p) > 5]

print(l2)