import pytest

from libpythonpro_ntg.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'niltonpimentel02@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'renzo@python.pro.br',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'niltonpimentel02']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'renzo@python.pro.br',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta.'
        )
