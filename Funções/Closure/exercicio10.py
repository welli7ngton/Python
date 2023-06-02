# Crie uma função chamada make_password_checker que recebe uma senha como argumento e retorna uma função interna. 
# A função interna deve receber uma senha fornecida pelo usuário e verificar se ela corresponde à senha original. 
# Teste a função retornada para verificar se as senhas estão corretas.


def make_password_checker(senha):
    def checker(senha2):
        
        if senha2 == senha:
            return "senha correta"
        else:
            return "senha incorreta"
    return checker


r = make_password_checker('123')

print(r("123"))