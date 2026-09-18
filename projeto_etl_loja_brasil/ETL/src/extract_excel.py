import openpyxl
import pandas as pd
from config import engine_dw

ARQUIVO = "dados/metas_vendas.xlsx"

df_metas = pd.read_excel(ARQUIVO)

def extrair_excel():
    print("Extraindo dados do arquivo Excel...")

    df_metas.to_sql(
        "metas_vendas",
        engine_dw,
        schema="bronze",
        if_exists="replace",
        index=False
    )
    print("Extração Excel concluída.")
    print("Dados gravados na camada BRONZE.")