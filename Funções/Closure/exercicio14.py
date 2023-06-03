# Crie uma função chamada make_calculator que retorna uma função interna. A função interna deve receber dois 
# números e um operador (como uma string) e retornar o resultado da operação matemática. Teste a função retornada ]
# para realizar diferentes operações matemáticas.

def make_calculator(n1,n2,op):
    def operacao():
        if op == "+":
            return n1 + n2
        elif op == "-":
            return n1 - n2
        elif op == "*":
            return n1 * n2
        elif op == "/":
            return n1 // n2
    return operacao

a = make_calculator(1, 2, "+")
b = make_calculator(10, 2, "-")
c = make_calculator(3, 2, "*")
d = make_calculator(6, 2, "/")

print(a())
print(b())
print(c())
print(d())

# saída:
#   3
#   8
#   6
#   3