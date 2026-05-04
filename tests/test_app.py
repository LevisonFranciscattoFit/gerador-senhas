import unittest
import string
import sys
import os

# Ajusta o caminho para importar o app corretamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import gerar_senha

class TestGeradorSenha(unittest.TestCase):

    def test_tamanho_senha(self):
        """Testa se o tamanho da senha gerada é igual ao solicitado."""
        tamanho = 12
        senha = gerar_senha(tamanho=tamanho, incluir_numeros=True, incluir_especiais=True)
        self.assertEqual(len(senha), tamanho)

    def test_caracteres_especiais(self):
        """Testa se a senha contém caracteres especiais quando solicitado."""
        senha = gerar_senha(tamanho=20, incluir_numeros=False, incluir_especiais=True)
        contem_especial = any(c in string.punctuation for c in senha)
        self.assertTrue(contem_especial)

    def test_apenas_letras(self):
        """Testa se a senha contém apenas letras quando números e especiais são desativados."""
        senha = gerar_senha(tamanho=15, incluir_numeros=False, incluir_especiais=False)
        self.assertTrue(senha.isalpha())

if __name__ == '__main__':
    unittest.main()