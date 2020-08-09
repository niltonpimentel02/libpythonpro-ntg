from libpythonpro_ntg.spam.enviador_de_email import Enviador
from libpythonpro_ntg.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'niltonpimentel02@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
