# Teoria

# polimorfismo é o princípio que permite que classes derivadas de uma mesma super classe tenham métodos iguais(com mesma assinatura) mas comportamentos diferentes.

# assinatura de método = mesmo nome e quantidade de parametros(o retorno não faz parte da assinatura)
# opinião + princípios que contam:
# SO "L" ID
# princípio da substituição de liskov
# objetos de uma superclasse devem ser substituiveis por objetos de uma subclasse sem quebrar a aplicação


# sobrecarga de métodos(overload) python não suporta
# sobreposição de métodos(override) python suporta

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self,mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print("E-mail: enviando:",self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print("SMS: enviando:",self.mensagem)
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("Notificação enviada")
    else:
        print("Notificação não enviada")

noti_email = NotificacaoEmail("Testando Email")
noti_SMS = NotificacaoSMS("Testando SMS")

notificar(noti_email)
notificar(noti_SMS)