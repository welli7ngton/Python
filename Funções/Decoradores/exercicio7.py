# 7- Escreva uma função decoradora chamada capitalize_result que modifique o resultado de uma 
# função para que a primeira letra seja maiúscula. Se o resultado for uma string, apenas a primeira 
# letra da string deve ser alterada para maiúscula. Se o resultado for uma lista de strings, a 
# primeira letra de cada string deve ser alterada para maiúscula.

def capitalize_result(funcao):
    def decoradora(*args):
        
        args = str(*args).replace("(","").replace(")","").replace("'","").replace(",","").split(" ")
        palavras_cap = [palavra.capitalize() for palavra in args]
        string_capitalizada = ""
        for _ in palavras_cap:
            string_capitalizada += (_ + " ")   
             
        return string_capitalizada 
    return(decoradora)


@capitalize_result
def recebe_strings(strings):    
    return True


strings = '''as revolucoes industriais tiveram um impacto significativo no mercado de trabalho ao longo da historia cada uma dessas revolucoes introduziu novas tecnologias metodos de produção e mudancas na organizacao do trabalho resultando em transformacoes no emprego e nas relacoes de trabalho.'''

print(recebe_strings(strings))

