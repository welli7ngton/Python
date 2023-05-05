try:
    value = input("Entre um valor: ")
    print(value/value)
except ValueError:
    print("Entrada incorreta...")
except ZeroDivisionError:
    print("Entrada muito ruim...")
except TypeError:
    print("muito muito ruim entrada...")
except:
    print("Booo!")