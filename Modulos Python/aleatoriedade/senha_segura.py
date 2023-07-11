from secrets import SystemRandom as Sr
import string

# todas as letras em Lower e High case, dígitos e pontuações
# print(string.ascii_letters, string.digits, string.punctuation)

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = "".join(Sr().choices(caracteres, k=8))

print(senha)
