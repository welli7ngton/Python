# context manager com função

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo,modo):
    try:
        print("Abrindo arquivo")
        arq = open(caminho_arquivo,modo)
        yield arq

    except Exception as e:
        print("Ocorreu erro")

    finally:
        print("Fechando arquivo")
        arq.close()


with my_open("aula150.txt","w") as arq:
    arq.write("Linha\n")
    arq.write("Linha\n",123)
    arq.write("Linha\n")
    print("WITH",arq)