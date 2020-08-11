from unittest.mock import Mock

import pytest

from libpythonpro_ntg.spam.main import EnviadorDeSpam
from libpythonpro_ntg.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Nilton', email='niltonpimentel02@gmail.com'),
            Usuario(nome='Renzo', email='niltonpimentel02@gmail.com')
        ],
        [
            Usuario(nome='Nilton', email='niltonpimentel02@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'niltonpimentel02@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Nilton', email='niltonpimentel02@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'renzo@python.pro.br',
        'niltonpimentel02@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
