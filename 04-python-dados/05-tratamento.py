import pandas as pd
import numpy as np


# ==========================
# 1. LEITURA DOS DADOS
# ==========================

clientes = pd.read_csv("clientes_sujos.csv")


# ==========================
# 2. LIMPEZA DOS DADOS
# ==========================

clientes["nome"] = clientes["nome"].str.strip().str.title()

clientes["cidade"] = clientes["cidade"].str.strip().str.title()


# ==========================
# 3. TRATAMENTO DE VALORES AUSENTES
# ==========================

clientes["idade"] = clientes["idade"].fillna(
    clientes["idade"].mean()
).astype(int)


# ==========================
# 4. CRIAÇÃO DE CATEGORIA
# ==========================

clientes["faixa_etaria"] = np.where(
    clientes["idade"] < 25,
    "Jovem",
    "Adulto"
)


# ==========================
# 5. VALIDAÇÃO DOS DADOS
# ==========================

print(clientes)

print(clientes.isna().sum())

print(clientes.dtypes)

print(clientes["idade"].min())

print(clientes["idade"].max())

print(clientes["cidade"].unique())
