from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from servicos.exportador import ExportadorService

class PaisesService:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") 
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=chrome_options)
        
    def abre_pagina(self, url: str):
        self.driver.get(url)
        print(f"Pagina aberta: {url}")

    def get_paises(self):
        lista_paises = []        

        paises = self.driver.find_elements(By.CLASS_NAME, "country")
        for pais in paises:
            name = pais.find_element(By.CLASS_NAME, "country-name").text
            capital = pais.find_element(By.CLASS_NAME, "country-capital").text
            populacao = pais.find_element(By.CLASS_NAME, "country-population").text
            area = pais.find_element(By.CLASS_NAME, "country-area").text
            print(f"Pais: {name}, Populacao: {populacao}")
            
            lista_paises.append({
                "name": name,
                "capital": capital,
                "population": populacao,
                "area": area
            })

        return lista_paises

    def fecha(self):
        self.driver.quit()
        print("Browser fechado.")