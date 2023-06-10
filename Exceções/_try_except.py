# Try, except, else e finally

try:
    b = int(input())
    a = 18
    c = a/b
except ZeroDivisionError:
    print("dividiu por 0.")
except IndexError:
    print("Index inválido.")
except ValueError as error:
    print("Msg:",error)
except TypeError as e:
    print("msg:", e)
else:
    print(c)
    