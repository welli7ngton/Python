# try except, else e finally

try:
    print(1)
    #print(8/0) # mesmo com esse erro
except ZeroDivisionError:
    print("Tratando o erro de divisão por 0.")
else:
    # o else será executado caso não ocorra nenhum erro ou tratamento de exceção no meio do programa.
    print("Não deu erro.")
finally:
    # o finally sempre é executado.
    print(2)