# Escreva uma função chamada make_name_generator que recebe um nome como argumento e retorna uma função interna. A 
# função interna deve receber um sobrenome e retornar o nome completo concatenado. Teste a função retornada para 
# gerar diferentes nomes completos.


def make_name_generator(nome):
    def gerador(sobrenome):
        nome_completo = "" 
        return nome_completo + (nome.title() +" "+ sobrenome.title())
    return gerador

a = make_name_generator("wellington")

print(a("almeida"))
print(a("silva"))

# saída:
# Wellington Almeida
# Wellington Silva