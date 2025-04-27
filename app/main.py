import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from servicos.paises_case import PaisesService
from servicos.exportador import ExportadorService

if __name__ == "__main__":
    servico_paises = PaisesService()
    URL = "https://www.scrapethissite.com/pages/simple/"
    servico_paises.abre_pagina(URL)
    lista_paises = servico_paises.get_paises()
    exportador = ExportadorService()
    exportador.exportar_para_csv("../compartilhado/paises.csv", ["name", "capital", "population", "area"], lista_paises)
    time.sleep(2)  
    servico_paises.fecha()

