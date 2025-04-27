import unittest
from unittest.mock import patch
from servicos.paises_case import PaisesService

class TestPaisesService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = PaisesService()
        cls.service.abre_pagina("https://www.scrapethissite.com/pages/simple/")
        cls.lista_paises = cls.service.get_paises()

    @classmethod
    def tearDownClass(cls):
        cls.service.fecha()

    def test_brasil_esta_na_lista(self):
        nomes_paises = [pais["name"] for pais in self.lista_paises]
        self.assertIn("Brazil", nomes_paises, "Brasil deveria estar na lista de países.")

    def test_lemuria_nao_esta_na_lista(self):
        nomes_paises = [pais["name"] for pais in self.lista_paises]
        self.assertNotIn("Lemuria", nomes_paises, "Lemuria não deveria estar na lista de países")

if __name__ == "__main__":
    unittest.main()