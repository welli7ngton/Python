# Herança Múltipla - Python POO
# Quer dizer que no Pyhton, uma classe pode estender várias outras classes.
# Herança Simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> Filelog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente

# Cliente(Pessoa,filelog)


class A:
    ...

    def quem_sou(self):
        print("A")
class B(A):
    ...

    # def quem_sou(self):
    #     print("B")
class C(A):
    ...

    def quem_sou(self):
        print("C")

class D(B,C):
    ...

    # def quem_sou(self):
    #     print("D")

d = D()
d.quem_sou()

print(D.mro())