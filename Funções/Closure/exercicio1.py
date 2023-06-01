# Crie uma função chamada multiply_by que recebe um número x e retorna uma função interna que multiplica qualquer 
# número dado por x. Teste a função retornada para multiplicar um número qualquer.

def multiply_by(x):
    def mult(y):
        return x * y
    
    return mult

a = multiply_by(2)

print(a(3))