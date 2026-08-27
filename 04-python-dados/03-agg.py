import pandas as pd


# ==========================
# 1. LEITURA DOS DADOS
# ==========================

clientes = pd.read_csv("clientes.csv")
vendas = pd.read_csv("vendas.csv")


# ==========================
# 2. LIMPEZA DOS DADOS
# ==========================

clientes["cidade"] = clientes["cidade"].str.title()


# ==========================
# 3. JUNÇÃO DOS DADOS
# ==========================

dados = clientes.merge(
    vendas,
    left_on="id",
    right_on="cliente_id"
)


# ==========================
# 4. AGREGAÇÃO
# ==========================

resultado = dados.groupby("cidade")["preco"].agg(
    ["sum", "mean", "count", "min", "max"]
)


# ==========================
# 5. ORGANIZAÇÃO DOS DADOS
# ==========================

resultado = resultado.rename(
    columns={
        "sum": "faturamento",
        "mean": "preco_medio",
        "count": "quantidade_vendas",
        "min": "menor_preco",
        "max": "maior_preco"
    }
)


# ==========================
# 6. VISUALIZAÇÃO
# ==========================

print(resultado)