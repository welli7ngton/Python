# Crie um menu que oferece duas opções ao usuário:
# "1. Calcular área do quadrado" e "2. Calcular área do círculo"
# Solicite a escolha do usuário e realize o cálculo da área com
# base na opção selecionada.
import time


class Exercicio3:
    @classmethod
    def _cls__init__(cls) -> None:
        while True:
            __class__.showMenu()
            respostaUsuario = int(input(""))
            if respostaUsuario == 1:
                __class__.calcSquare()
            elif respostaUsuario == 2:
                __class__.calcCircle()
            elif respostaUsuario == 3:
                __class__.calcTrapeze()
            elif respostaUsuario == 4:
                print("Programa encerrado.")
                break
            else:
                print("Digite um valor válido.")

    @classmethod
    def showMenu(cls) -> None:
        time.sleep(2)
        print("Escolha uma opção:")
        print("1 - Calcular área do quadrado.")
        print("2 - Calcular área do círculo.")
        print("3 - Calcular área do trapézio.")
        print("4 - Encerrar programa.")

    @classmethod
    def calcSquare(cls) -> None:
        largura = float(input("Digite a largura do quadrado: "))
        altura = float(input("Digite a altura do quadrado: "))
        print(f"A área do quadrado é: {altura * largura}.")

    @classmethod
    def calcCircle(cls) -> None:
        PI = 3.14
        raio = float(input("Digite o raio do círculo: "))
        print(f"A área do círculo é: {PI * (raio**2)}")

    @classmethod
    def calcTrapeze(cls) -> None:
        baseMaior = float(input("Digite a base maior: "))
        baseMenor = float(input("Digite a base menor: "))
        altura = float(input("Digite a altura: "))
        print(f"A área do trapézio é: {((baseMaior + baseMenor)* altura)/2}")


if __name__ == '__main__':
    Exercicio3._cls__init__()
