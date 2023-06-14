# 9- Crie uma função decoradora chamada accepts que verifique se os argumentos de uma função são do tipo 
# esperado. A função decoradora deve aceitar os tipos esperados como argumentos e lançar uma exceção se algum 
# argumento não corresponder ao tipo esperado.


def accepts(função):
    def decoradora(*args):
        for arg in args:
            if not isinstance(arg,int):
                raise Exception(f"Argumento:({arg}) não é do tipo Inteiro ou Float")
        return função(*args)
    return decoradora


@accepts
def soma(x,y):
    return x+y

soma(1,2)