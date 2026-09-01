import pandas as pd
import numpy as np


# ==========================
# 1. LEITURA DOS DADOS
# ==========================

def carregar_dados(arquivo):
    clientes = pd.read_csv(arquivo)
    return clientes


# ==========================
# 2. TRATAMENTO DOS DADOS
# ==========================

def tratar_clientes(clientes):
    clientes["nome"] = clientes["nome"].str.strip().str.title()

    clientes["cidade"] = clientes["cidade"].str.strip().str.title()

    clientes["idade"] = clientes["idade"].fillna(
        clientes["idade"].mean()
    ).astype(int)

    return clientes


# ==========================
# 3. TRANSFORMAÇÃO DOS DADOS
# ==========================

def transformar_clientes(clientes):
    clientes["faixa_etaria"] = np.where(
        clientes["idade"] < 25,
        "Jovem",
        "Adulto"
    )

    return clientes


# ==========================
# 4. VALIDAÇÃO DOS DADOS
# ==========================

def validar_clientes(clientes):
    print("Valores ausentes:")
    print(clientes.isna().sum())

    print("\nTipos das colunas:")
    print(clientes.dtypes)


# ==========================
# 5. EXPORTAÇÃO DOS DADOS
# ==========================

def salvar_clientes(clientes):
    clientes.to_csv(
        "clientes_tratados.csv",
        index=False
    )


# ==========================
# 6. FUNÇÃO AUXILIAR
# ==========================

def contar_clientes(clientes):
    total_clientes = len(clientes)

    print("Total de clientes:", total_clientes)


# ==========================
# 7. EXECUÇÃO DO PIPELINE
# ==========================

if __name__ == "__main__":
    clientes = carregar_dados("clientes_sujos.csv")

    clientes = tratar_clientes(clientes)

    clientes = transformar_clientes(clientes)

    validar_clientes(clientes)

    salvar_clientes(clientes)

    print(clientes)

    contar_clientes(clientes)
