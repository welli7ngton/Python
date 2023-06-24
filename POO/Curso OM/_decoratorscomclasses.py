# funcoes decoradoras e decoradores com classes

# a função add_repr foi criada para receber uma classe
# dentro de ad_repr foi definida uma função para receber p self da classe adicionada em add_repr
# dentro de meu_rp foram criadas as variáveis para armazenar o nome da classe e os atributos das instancias
# a função meu_rp retorna o repr como uma string formatada
# na linha antes do retorno da função add_repr a propria classe é chamada com seu atributo __repr__ para receber o retorno da função meu_rp
def add_repr(cls):
    def meu_rp(self):
        nome_classe =  self.__class__.__name__
        dict_classe = self.__dict__
        repr_classe =  f"{nome_classe}({dict_classe})"
        return repr_classe
    cls.__repr__ = meu_rp
    return cls

@add_repr
class Time:

    def __init__(self,nome):
        self.nome = nome

@add_repr
class Planeta:

    def __init__(self,nome):
        self.nome = nome

brasil = Time("Brasil")
portugal = Time("Portugal")

terra = Planeta("Terra")
marte = Planeta("Marte")


print(brasil)
print(portugal)
print(terra)
print(marte)