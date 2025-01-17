import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../../src')))


from media_aprovacao import calcular_aprovacao


@pytest.mark.parametrize("n1, n2, n3, esperado", [
    (0,0,0, "reprovado"),(0.1,0.1,0.1, "reprovado"),(4.8,4.8,4.8, "reprovado"),
    (4.9,4.9,4.9, "reprovado"),(5,5,5, "prova final"),(5.1,5.1,5.1, "prova final"),
    (6.8,6.8,6.8, "prova final"),(6.9,6.9,6.9, "prova final"),
    (7,7,7, "aprovado"),(7.1,7.1,7.1, "aprovado"),(9.9,9.9,9.9, "aprovado"),
    (10,10,10, "aprovado")
])
def test_calcular_aprovacao_parametrize(n1, n2, n3, esperado):
    calcular_aprovacao(n1, n2, n3) == esperado

def test_calcular_aprovacao():
    with pytest.raises(ValueError, match="média incorreta"):
        calcular_aprovacao(-0.9,-0.9,-0.9)
        calcular_aprovacao(10.1,10.1,10.1)