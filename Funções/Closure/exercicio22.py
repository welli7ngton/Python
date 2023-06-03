# Escreva uma função chamada make_password_validator que recebe uma senha como argumento e retorna uma função 
# interna. A função interna deve receber uma senha fornecida pelo usuário e retornar se ela corresponde ou não à 
# senha original. Teste a função retornada para validar diferentes senhas.


def make_password_validator(senha):
    def validador(user_input):
        if user_input == senha:
            return True
        else:
            return False
    return validador


a = make_password_validator("123456")
print(a("1234567"))
print(a("123456"))
print(a("12345"))

# saída:
# False
# True
# False