import csv

class ExportadorService:

    def __init__(self):
        pass

    def exportar_para_csv(self, arquivo, cabecalho, dados):
        try:
            with open(arquivo, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=cabecalho)
                writer.writeheader()
                writer.writerows(dados)
            print(f"Dados exportados com sucesso para {arquivo}")
        except Exception as e:
            print(f"Erro ao exportar para CSV: {e}")