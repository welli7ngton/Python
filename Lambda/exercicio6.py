# 6-Escreva uma expressão lambda que verifique se uma string é um palíndromo.


def executa(funcao,args):
    return funcao(args)

palavra = "1112111"

print(executa(lambda x: True if x[::-1] == x else False,palavra))

a = lambda p: True if p[::-1] == p else False

print(a("wellington"))
print(a("1001"))
print(a("1111"))
print(a("subinoonibus"))

