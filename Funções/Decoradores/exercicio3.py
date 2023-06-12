# 3- Crie uma função decoradora chamada validate_args que verifique se os argumentos de uma função 
# estão corretos. Ela deve receber uma função alvo como argumento e uma lista de validações. Cada 
# validação deve ser uma tupla com o índice do argumento e uma função de validação. Se algum 
# argumento não passar na validação correspondente, a função decorada deve lançar uma exceção.

def validate_args(lista_validacoes):
    def decoradora(funcao):
        def execucao(*args):
            c = 0
            while c < len(lista_validacoes):
              
                fun = lista_validacoes[c][1]
                if not fun(args[c]):
                    raise Exception("Não é válido.")
                else:
                    print(f"Validação {c+1} completa.")      
                c += 1
            print(funcao(*args)) 
        return execucao
      
    return decoradora

@validate_args(lista_validacoes= [(0,lambda x: True if isinstance(x,int) else False),(1,lambda x: True if isinstance(x,float) else False),(2,lambda x: True if isinstance(x,str) else False)])

def fun_alvo(int1,flt2,str3):
    return "Código válido."

fun_alvo(1,2.0,"palavra")

fun_alvo(3,5.0,6)